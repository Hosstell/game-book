from abc import ABC, abstractmethod
import json


class Keyboard(ABC):
    @abstractmethod
    def create_keyboard(self, *args, **kwargs):
        pass


class VKKeyboard(Keyboard):
    @staticmethod
    def create_keyboard(data):
        buttons = []
        for link in data['links']:
            buttons.append([{
                'name': link['text'],
                'callback': 'next_to|{}'.format(link['to']),
                'color': 'positive'
            }])

        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                buttons[i][j] = VKKeyboard.convert(buttons[i][j])

        keyboard = {
            "one_time": None,
            "buttons": buttons
        }

        return json.dumps(keyboard, ensure_ascii=False)

    @staticmethod
    def convert(button):
        return {
            "action": {
                "type": "text",
                "payload": json.dumps(button['callback']),
                "label": button['name']
            },
            "color": button['color']
        }
