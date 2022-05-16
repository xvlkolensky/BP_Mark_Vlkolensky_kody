from json import loads
from actions.messenger import make_request
from message_router import process_message
from jeevesDB.database import initialize_database

from aiokafka import AIOKafkaConsumer
import asyncio

async def startup():
    await initialize_database()

async def consume():

    consumer = AIOKafkaConsumer(
        'database',
        bootstrap_servers=['192.168.5.129:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))

    await startup()
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for message in consumer:
            message = message.value
            print(f"this is the message we got{message}")
            metadata = message["metadata"]
            data = message["data"]
            msg_title=message["data"]["title"]

            if msg_title=="get_user_location_for_weather":
                message["data"]["title"]="get_user_location"

            title,data = await process_message(data, metadata)

            if msg_title=="get_user_location_for_weather":
                title="to_weather"

            info = {
                "title":title,
                "data":data
            }
            packet = {
                "metadata": metadata,
                "data": info
            }

            print(f"this is the packet we will send out {packet}")

            await make_request("", packet)

    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()


asyncio.run(consume())
