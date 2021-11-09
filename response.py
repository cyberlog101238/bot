from datetime import datetime

def sample_responses(input_text):
    user_massage = str(input_text).lower()

    if user_massage in ("hello"):
        return "Hey! How are you?"

    return "Hey! Run /help"
