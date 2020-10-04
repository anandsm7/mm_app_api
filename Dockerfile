FROM python:3.7-alpine
MAINTAINER anandsm7

#makes python show all logs within docker
ENV PYTHONUNBUFFERED 1 
COPY ./requirements.txt /requirements.txt 
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

#security
RUN adduser -D user
USER user
