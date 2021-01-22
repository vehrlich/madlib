FROM python:3-alpine

RUN mkdir /app
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/

RUN chmod -R a+rwx .


ENV PYTHONBUFFERED 1
