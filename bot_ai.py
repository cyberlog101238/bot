from bot_brain import*

# Commands
help = "/ss <url> to take sceenshot..(/ss https://www.google.com"
start = "Welcome!\nLet's get start... \n\nowener: @jabir52"

def bot_ai(message):
    message = message.lower()
    is_tag_user = "n"
    if message in a:
        is_tag_user = "y"
        return a[message], is_tag_user
    elif "hi" in "message":
        is_tag_user = "y"
        return a["hi"], is_tag_user
    elif "hello" in message:
        is_tag_user = "y"
        return a["hello"], is_tag_user
    elif "/help" in message:
        return help, is_tag_user
    elif "/start" in message:
        return start, is_tag_user





    return "Opps! \nMessages was not found in my brain", is_tag_user



