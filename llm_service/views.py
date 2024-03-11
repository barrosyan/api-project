import os
import sys
import tempfile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from langchain_community.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings
from langchain import PromptTemplate
from langchain.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from django.shortcuts import render

class SuppressStdout:
    def __enter__(self):
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
        sys.stderr = self._original_stderr

@csrf_exempt
def llm_view(request):
    if request.method == 'POST' and request.FILES.get('pdf_file') and request.POST.get('context') and request.POST.get('question'):
        pdf_file = request.FILES['pdf_file']
        context = request.POST['context']
        question = request.POST['question']

        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
            for chunk in pdf_file.chunks():
                temp_pdf.write(chunk)
            temp_pdf_path = temp_pdf.name

        loader = PyPDFLoader(temp_pdf_path)
        pages = loader.load_and_split()

        from langchain.text_splitter import RecursiveCharacterTextSplitter
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        all_splits = text_splitter.split_documents(pages)

        with SuppressStdout():
            vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())

        template = """Use the following pieces of context to answer the question at the end. 
        If you don't know the answer, just say that you don't know, don't try to make up an answer. 
        Use three sentences maximum and keep the answer as concise as possible. 
        {context}
        Question: {question}
        Helpful Answer:"""
        QA_CHAIN_PROMPT = PromptTemplate(
            input_variables=["context", "question"],
            template=template,
        )

        llm = Ollama(model="llama2:13b")
        chain = QA_CHAIN_PROMPT | llm | StrOutputParser()
        response = chain.invoke({
            "context": context,
            "question": question
        })

        return JsonResponse({'response': response})
    else:
        return render(request, 'llm_form.html')