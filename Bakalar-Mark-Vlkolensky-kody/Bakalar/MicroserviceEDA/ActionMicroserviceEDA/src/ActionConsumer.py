from kafka import KafkaConsumer
from json import loads
from messenger import make_request
from message_router import process_message

from aiokafka import AIOKafkaConsumer
import asyncio


async def consume():
    consumer = AIOKafkaConsumer(
        'actions',
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
            print(message)
            metadata = message["metadata"]
            data = message["data"]
            data = await process_message(data, metadata)
            packet = {
                "metadata": metadata,
                "data": data
            }

            url = r"http://127.0.0.1:5002/slack_post"
            if message["data"]["title"]=='slack_post':
                await make_request(url, packet)

            print(f'{message} added to arr')
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()


asyncio.run(consume())
