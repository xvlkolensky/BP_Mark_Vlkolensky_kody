from jeevesDB.database import user_dal


async def register_user(message):
    request_body = message
    print(request_body)
    print(request_body["data"]["data"]["name"])
    print(request_body["data"]["data"]["location"])
    async with user_dal() as ud:
        await ud.create_user(request_body["data"]["data"]["name"],request_body["metadata"]["sender"],request_body["data"]["data"]["location"])
    return "user has been registered"

async def change_name(message):
    request_body = message
    print(request_body)

    async with user_dal() as ud:
        await ud.change_name(request_body["metadata"]["sender"],request_body["data"]["data"])
    return "changed"


async def change_location(message):
    request_body = message

    print("CHANGE LOCATION")
    print(request_body)

    async with user_dal() as ud:
        await ud.change_location(request_body["metadata"]["sender"],request_body["data"]["data"])
    return f"changed location to {request_body['data']['data']}"


async def get_user_location(message):
    request_body = message

    print(f"message : {request_body}")

    async with user_dal() as ud:
        location = await ud.get_user_location(request_body["metadata"]["sender"])
    return location