# clientsession.py
import asyncio
import aiohttp

async def make_request(url,data):
    headers = {
        "Content-Type": "application/json",
    }

    url = r"http://127.0.0.1:5001/actions"

    print(data)

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url,json=data) as response:
            print(await response.text())
