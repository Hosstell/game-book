from listener import VKListener
from book import Book


class VKHandler(VKListener):
    def __init__(self):
        super(VKHandler, self).__init__()
        self.book = Book('./books/book.txt')

    def handler(self, user_id, text, payload):
        if payload:
            next_step = payload.split('|')[-1]
            next_step_data = self.book[next_step]
            return next_step_data


if __name__ == '__main__':
    a = VKHandler()
    a.run()
