# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /API
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV QUART_APP=API:app

CMD [ "quart", "run", "--host=0.0.0.0"]