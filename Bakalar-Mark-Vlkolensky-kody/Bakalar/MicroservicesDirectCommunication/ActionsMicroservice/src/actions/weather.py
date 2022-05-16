from .messenger import make_request,make_request_for_return

async def get_user_location(message,metadata):
    url = r"http://127.0.0.1:5003/get_user_location"
    location = await make_request_for_return(url,{"metadata":metadata,"data":message})
    print(f"user location from response {location}")
    return location

async def weather_info(message,metadata):
    url = r"http://127.0.0.1:5004/weather"

    location = await get_user_location(message,metadata)
    print(location)
    location = await make_request_for_return(url, {"metadata": metadata, "data": location})

    return location