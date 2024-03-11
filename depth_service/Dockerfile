FROM python:3.9-slim

WORKDIR /app

COPY ../manage.py /app/manage.py

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --upgrade django \
    && pip install --upgrade setuptools \
    && pip install wheel \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001

WORKDIR /app/vitrus

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
