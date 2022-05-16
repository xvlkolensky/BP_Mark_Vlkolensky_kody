from ..actions.misc import do_the_thing
from ..actions.help import show_help_text
from ..actions.register_user import  register_user,get_user_location
from ..actions.weather import weather_info
from ..actions.register_user import change_name,change_location


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

    print(f"In process message with '{message}'")
    for test, action in ACTION_MAP.items():
        if message.startswith(test):
            print(f"Working on {test}")
            reply = await action(message.lstrip(test), metadata)
            print(f'reply {reply}')
            break

    if reply is None:
        reply=message

    return reply
