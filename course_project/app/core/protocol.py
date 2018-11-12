from typing import Callable, Optional
import textwrap


def indent(text, amount, ch=' '):
    return textwrap.indent(text, amount * ch)


class Protocol:
    """ Класс для ведения протокола - экземпляр передается классификатору, тот добавляет сообщения """

    def __init__(self, update: Callable[['Protocol'], None]):
        self.messages = []
        self.update = update
        self._indent = 0

    @property
    def last_message(self) -> Optional[str]:
        return self.messages[-1] if len(self.messages) else None

    def __call__(self, message: str):
        self.messages.append(indent(message, self._indent))
        self.update(self)

        return self

    def __enter__(self):
        self._indent += 4
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._indent -= 4
