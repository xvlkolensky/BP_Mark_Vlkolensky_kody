from quart import Blueprint, request
from ..outgoing.slack import post_to_slack

slackpost = Blueprint("actions", __name__)

@slackpost.route("/slack_post", methods=["POST"])
async def my_post_handler():
    request_body = await request.get_json()
    print(request_body)
    post_to_slack(request_body["data"],request_body["metadata"])
    return "ok", 200