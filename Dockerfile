FROM python:3

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt
