from quart import Blueprint, request
from ..actions.messenger import make_request
from ..controller.message_router import process_message


actions = Blueprint("actions", __name__)


@actions.route("/actions", methods=["POST"])
async def my_post_handler():
    request_body = await request.get_json()
    metadata = request_body["metadata"]
    data = request_body["data"]
    data = await process_message(data,metadata)
    print(data)
    packet = {
        "metadata":metadata,
        "data": data
    }
    print(packet)
    url = r"http://127.0.0.1:5002/slack_post"
    await make_request(url,packet)
    return "ok", 200