import requests

def kelvin_to_celsius(kelvin):
    return int(kelvin - 273.15)


def process_weather_response(weather_data):
    temperature = kelvin_to_celsius(weather_data["main"]["temp"])
    feels_like = kelvin_to_celsius(weather_data["main"]["feels_like"])
    return f"The temperature is {temperature}℃ and it feels like {feels_like}℃"


async def fetch_weather(location):

    text=location

    url = "https://api.openweathermap.org/data/2.5/weather?q={text}&appid={token}".format(
        text=text, token="e877bd486a6fedea25e3effe0b58614c")

    response = requests.get(url)
    print(response.json())
    response.raise_for_status()
    return process_weather_response(response.json())
