# clientsession.py
import asyncio
import aiohttp
from json import dumps
from kafka import KafkaProducer

async def make_request_for_return(url,data):
    headers = {
        "Content-Type": "application/json",
    }

    print(data)

    # url = r"http://127.0.0.1:5002/slack_post"

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, json=data) as response:
            print(await response.text())
            response_text = await response.text()
            print(f"This is the response {response_text}")
            return response_text


producer = KafkaProducer(bootstrap_servers=['192.168.5.129:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

async def make_request(url,data):
    headers = {
        "Content-Type": "application/json",
    }

    print(data)

    producer.send('slack_post', value=data)