from messenger import make_request,make_request_for_return
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['192.168.5.129:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

async def change_name(message,metadata):
    title = "change_name"
    data = message.split(" ")
    name = data[1]
    data["title"]=title
    data["data"]=name

    message = {
        "metadata":metadata,
        "data":data
    }

    print(message)
    producer.send('database', value=message)

async def change_location(message,metadata):
    title = "change_location"
    msg = message["data"]
    data = msg.split(" ")
    location = data[1]
    data = {}
    data["title"] = title
    data["data"] = location

    message = {
        "metadata": metadata,
        "data": data
    }

    print(data)
    print(message)
    producer.send('database', value=message)


async def get_user_location(message,metadata):
    title = "get_user_location"
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

async def register_user(message, metadata):
    user = metadata["sender"]
    msg =message["data"]
    data = msg.split(" ")

    print(data)

    name = data[1]
    location = data[2]

    info = {
        "name":name,
        "location":location
    }

    title = r"register_user"

    data={}

    data["title"] = title
    data["data"] = info

    message = {
        "metadata": metadata,
        "data": data
    }

    print(data)
    print(message)
    producer.send('database', value=message)