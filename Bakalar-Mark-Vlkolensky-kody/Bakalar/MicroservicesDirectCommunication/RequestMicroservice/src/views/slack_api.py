
from quart import Blueprint, request

# from ..controller.message_router import process_message
from ..actions.messenger import make_request

# Respond to the SlackBot setup challenge

slack_api = Blueprint("api", __name__)


def respond_to_slack_challenge(incoming_challenge):
    return {"challange":incoming_challenge.get("challenge", "")}, 200


def extract_slack_text(request_body):
    # Deep JSON structure
    elements = request_body["event"]["blocks"][0]["elements"][0]["elements"]
    for part in elements:
        if part["type"] == "text":
            return part["text"].lstrip()

    return request_body["event"]["text"].partition(">")[2].lstrip()


def outgoing_metadata(request_body):
    return {
        "type": "slack",
        "message_type": request_body["event"]["type"],
        "team": request_body["event"]["team"],
        "sender": request_body["event"]["user"],
        "channel": request_body["event"]["channel"],
        "ts": request_body["event"]["ts"],  # used for replies
    }


@slack_api.route("/slack", methods=["POST"])
async def incoming_slack_endpoint():
    """Receive an event from Slack."""

    request_body = await request.get_json()

    # When setting up a Slack app, we are sent a verification
    # challenge, and we must respond with the token provided.
    print(request_body)
    if request_body.get("type", "") == "url_verification":
        return respond_to_slack_challenge(request_body)

    metadata = outgoing_metadata(request_body)
    data = extract_slack_text(request_body)

    packet = {
        "metadata": metadata,
        "data": data
    }

    print("Received message: %s", extract_slack_text(request_body))
    await make_request("http://127.0.0.1:5001/actions",packet)
    # await process_message(
    #    extract_slack_text(request_body), outgoing_metadata(request_body)
    # )
    # Slack ignores the data here, but a value may help our debugging.
    return {"status": "OK"}, 200
