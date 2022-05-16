from json import loads
from messenger import make_request
from weather import fetch_weather

from aiokafka import AIOKafkaConsumer
import asyncio


async def consume():
    consumer = AIOKafkaConsumer(
        'weather',
        bootstrap_servers=['192.168.5.129:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for message in consumer:
            message = message.value
            print(f"weather got this message {message}")
            metadata = message["metadata"]
            data = message["data"]["data"]["data"]
            reply = await fetch_weather(data)

            info = {
                "title":"slack_post",
                "data":reply
            }

            packet = {
                "metadata": metadata,
                "data": info
            }

            url = r"http://127.0.0.1:5002/slack_post"
            await make_request(url, packet)

            print(f'{message} added to arr')
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()


asyncio.run(consume())
