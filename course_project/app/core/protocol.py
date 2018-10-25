from typing import Callable


class Protocol:
    """ Класс для ведения протокола - экземпляр передается классификатору, тот добавляет сообщения """

    def __init__(self, update: Callable[['Protocol'], None]):
        self.messages = []
        self.update = update

    @property
    def last_message(self):
        return self.messages[-1] if len(self.messages) else None

    def add_message(self, message):
        self.messages.append(message)
        self.update(self)
