FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
ENV TZ=UTC
WORKDIR  /app
RUN pip install --upgrade pip setuptools
COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app



