from .messenger import make_request,make_request_for_return

async def change_name(message,metadata):
    url = r"http://127.0.0.1:5003/change_name"
    data = message.split(" ")

    print(data)

    name = data[1]

    location = await make_request_for_return(url, {"metadata": metadata, "data": name})
    print(f"user location from response {location}")
    return f"user location is {location}"

async def change_location(message,metadata):
    url = r"http://127.0.0.1:5003/change_location"
    data = message.split(" ")

    print(data)

    location = data[1]

    print(f"Name {location}")

    location = await make_request_for_return(url, {"metadata": metadata, "data": location})
    print(f"user location changed {location}")
    return location


async def get_user_location(message,metadata):
    url = r"http://127.0.0.1:5003/get_user_location"
    location = await make_request_for_return(url,{"metadata":metadata,"data":message})
    print(f"user location from response {location}")
    return f"user location is {location}"

async def register_user(message, metadata):
    user = metadata["sender"]

    data = message.split(" ")

    print(data)

    name = data[1]
    location = data[2]

    info = {
        "name":name,
        "location":location
    }

    url = r"http://127.0.0.1:5003/register_user"

    packet = {
        "metadata":metadata,
        "data":info
    }

    await make_request(url,packet)

    return f"Hi there {name} from {location}"
