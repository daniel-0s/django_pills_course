FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1 

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev 
RUN pip install psycopg2

RUN mkdir /app
WORKDIR /app

COPY  requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

# RUN adduser -D user
# USER user
