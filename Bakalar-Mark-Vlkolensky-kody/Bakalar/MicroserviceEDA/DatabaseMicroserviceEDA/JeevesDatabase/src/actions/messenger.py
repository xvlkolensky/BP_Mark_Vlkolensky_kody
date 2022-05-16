# clientsession.py
import asyncio
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['192.168.5.129:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

async def make_request(url,data):
    headers = {
        "Content-Type": "application/json",
    }

    url = r"http://127.0.0.1:5001/actions"

    print(data)

    producer.send('actions', value=data)
