from quart import Blueprint, redirect, render_template, request
from ..jeevesDB.database import user_dal

user = Blueprint("user", __name__)


@user.get("/users/<int:user_id>")
async def get_user(user_id):
    async with user_dal() as ud:
        return await ud.get_user(user_id)

# """
# Toto nefunguje error in http_stream


@user.get("/users")
async def get_all_users():
    async with user_dal() as ud:
        return await ud.get_all_users()
# """

@user.post("/register_user")
async def register_user():
    request_body = await request.get_json()
    print(request_body)
    print(request_body["data"]["name"])
    print(request_body["data"]["location"])
    async with user_dal() as ud:
        await ud.create_user(request_body["data"]["name"],request_body["metadata"]["sender"],request_body["data"]["location"])
    return "user has been registered"

@user.post("/change_name")
async def change_name():
    request_body = await request.get_json()

    async with user_dal() as ud:
        await ud.change_name(request_body["metadata"]["sender"],request_body["data"])
    return "changed"

@user.post("/change_location")
async def change_location():
    request_body = await request.get_json()

    print("CHANGE LOCATION")
    print(request_body)

    async with user_dal() as ud:
        await ud.change_location(request_body["metadata"]["sender"],request_body["data"])
    return f"changed location to {request_body['data']}"



@user.post("/get_user_location")
async def get_user_location():
    request_body = await request.get_json()

    async with user_dal() as ud:
        location = await ud.get_user_location(request_body["metadata"]["sender"])
    return location