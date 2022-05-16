# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV QUART_APP=src:app

CMD [ "quart", "run", "--host=0.0.0.0", "--port=5002"]