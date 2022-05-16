from misc import do_the_thing
from help import show_help_text
from register_user import  register_user,get_user_location
from weather import weather_info,get_weather
from register_user import change_name,change_location

ACTION_MAP = {
    "help": show_help_text,
    "misc": do_the_thing,
    "register": register_user,
    "get_location":get_user_location,
    "weather_info": weather_info,
    "change_name": change_name,
    "change_location":change_location
    # "signin": direct_user_to_web,
}

async def process_message(message, metadata):
    """Decide on an action for a chat message.

    Arguments:
        message (str): The body of the chat message
        metadata (dict): Data about who sent the message,
              the time and channel.
    """
    reply = None

    if message["title"]=="to_weather":
        await get_weather(message, metadata)
        return message

    msg=message["data"]


    print(f"In process message with '{message}'")
    for test, action in ACTION_MAP.items():
        if msg.startswith(test):
            print(f"Working on {test}")
            reply = await action(message, metadata)
            print(f'reply {reply}')
            break

    if reply is None:
        reply=message

    return reply
