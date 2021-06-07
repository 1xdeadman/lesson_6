from typing import Any


class Test:

    def __init__(self):
        data: list[float] = list()

    def add(self, value: Any) -> None:
        """ Заносит в список data значение value, обеспечивая, что в списке будут храниться только те данные, которые
        указаны в его аннотации типа.

        :param value: хранимое значение
        :return:
        """