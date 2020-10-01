import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import settings
import logging
import datetime
import time
from keyboard import VKKeyboard
from threading import Thread
from abc import ABC, abstractmethod

logging.basicConfig(filename="logging.log", level=logging.INFO)


def log(event):
    payload = getattr(event, 'payload', None)
    string = '{} - {}: {}({})'.format(datetime.datetime.now(), event.user_id, event.text, payload)
    logging.info(string)


class Listener(ABC):
    @abstractmethod
    def run(self):
        pass


class VKListener(Listener, Thread):
    def __init__(self):
        super(Listener, self).__init__()
        vk_session = vk_api.VkApi(token=settings.group_token)
        self.vk = vk_session.get_api()
        self.longpoll = VkLongPoll(vk_session)

    def run(self):
        print('It is work!')
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                text = event.text
                payload = getattr(event, 'payload', None)
                payload = payload[1:-1] if payload else payload
                payload = payload or '1'
                user_id = event.user_id

                data = self.handler(user_id, text, payload)
                self.send_message(user_id, data)

                log(event)

    def handler(self, user_id, text, payload):
        pass

    def send_message(self, user_id, data):
        if data:
            keyboard = VKKeyboard.create_keyboard(data)
            self.vk.messages.send(
                user_id=user_id,
                keyboard=keyboard,
                message=data['text'],
                random_id=str(time.time())
            )

