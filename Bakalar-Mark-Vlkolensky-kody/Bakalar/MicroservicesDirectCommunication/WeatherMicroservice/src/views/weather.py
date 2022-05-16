import requests
from quart import Blueprint, request
from ..actions.weather import fetch_weather


weather = Blueprint("weather", __name__)

@weather.post("/weather")
async def get_weather():
    request_body = await request.get_json()
    data = await fetch_weather(request_body["data"])
    print(f"return in weather microservice : {data}")
    return data