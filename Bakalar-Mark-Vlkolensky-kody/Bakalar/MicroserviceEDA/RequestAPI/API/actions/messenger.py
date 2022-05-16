# clientsession.py
import asyncio
import aiohttp
from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['192.168.5.129:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

async def make_request(url,message,metadata):
    headers = {
        "Content-Type": "application/json",
    }

    title = "actions"

    info={
        "title":title,
        "data":message
    }

    data={
        "metadata":metadata,
        "data":info
    }

    print(data)

    producer.send('actions', value=data)
