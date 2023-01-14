from telebot import types


def create_keyboard(data):
    keyboard = types.InlineKeyboardMarkup()
    for action in data['actions']:
        btn = types.InlineKeyboardButton(callback_data=action["redirect_to"], text=action["text"])
        keyboard.add(btn)
    return keyboard
