from db_interaction import register_user,change_name,change_location,get_user_location


ACTION_MAP = {
    "register_user": register_user,
    "change_name": change_name,
    "change_location": change_location,
    "get_user_location":get_user_location,
}

async def process_message(message, metadata):
    """Decide on an action for a chat message.

    Arguments:
        message (str): The body of the chat message
        metadata (dict): Data about who sent the message,
              the time and channel.
    """
    reply = None

    msg = message["title"]

    packet = {
        "metadata":metadata,
        "data":message
    }

    title = 'slack_post'

    print(f"In process message with '{message}'")
    for test, action in ACTION_MAP.items():
        if msg.startswith(test):
            print(f"Working on {test}")
            reply = await action(packet)
            print(f'reply {reply}')
            break

    if reply is None:
        reply=message

    return title,reply
