from messenger import make_request,make_request_for_return

from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['192.168.5.129:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


async def get_user_location(message, metadata):
    title = "get_user_location_for_weather"
    data = {}
    data["title"] = title
    data["data"] = message

    message = {
        "metadata": metadata,
        "data": data
    }

    print(data)
    print(message)
    producer.send('database', value=message)


async def weather_info(message,metadata):
    await get_user_location(message,metadata)

async def get_weather(message,metadata):
    title="weather"
    data={}
    data["title"]=title
    data["data"]=message
    message={
        "metadata":metadata,
        "data":data
    }
    print(message)
    producer.send('weather',value=message)