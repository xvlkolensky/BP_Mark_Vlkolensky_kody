# clientsession.py
import asyncio
import aiohttp

async def make_request(url,data):
    headers = {
        "Content-Type": "application/json",
    }

    print(data)

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url,data) as response:
            print(await response.text())
