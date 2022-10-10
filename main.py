import telebot

from books.books import create_book
from settings import group_token, book_name
from keyboard import create_keyboard

bot = telebot.TeleBot(group_token)
book = create_book(book_name)


def reply_to_message(message, next_page):
    page_data = book.get_page(next_page)
    keyboard = create_keyboard(page_data)
    bot.send_message(message.chat.id, page_data["text"], reply_markup=keyboard)


@bot.message_handler(commands=["start"])
def start(message):
    reply_to_message(message, 1)


@bot.message_handler(content_types=["text"])
def start(message):
    reply_to_message(message, 1)


@bot.callback_query_handler(lambda query: True)
def callback_query_handler(data):
    next_page = int(data.data)
    reply_to_message(data.message, next_page)
    return True


bot.polling(none_stop=True, interval=0)
