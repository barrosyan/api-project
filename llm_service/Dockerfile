FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
COPY * .

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install wheel
RUN pip install --upgrade django
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8002

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]