"""
TODO: написать тесты для данного модуля.
"""
from typing import Optional


class Database:
    QUEUE_MAX_SIZE = 5

    def __init__(self):
        self._first_queue = []
        self._second_queue = []

    def find_student_position(self, username: str) -> tuple[int, int, int]:
        """ Ищет студента в никнеймом username  в очередях

        :param username: имя искомого студента
        :return: Кортеж из трех значений [pos, priority_size, common_size]:
            - pos: индекс студента в очереди, -1 если студента нет в очереди
            - priority_size: размер приоритетной очереди
            - common_size: размер обычной очереди
        """
        user_index = -1
        max_count = max(len(self._first_queue), len(self._second_queue))
        for index in range(max_count):
            if len(self._first_queue) > max_count and self._first_queue[index][0] == username:
                user_index = index
                break
            if len(self._second_queue) > max_count and self._second_queue[index][0] == username:
                user_index = len(self._first_queue) + index
                break
        return user_index, len(self._first_queue), len(self._second_queue)

    def add_student(self, username: str, displayed_username: str):
        """Добавляет студента в обычную очередь.

        Если общий размер очередей превышает QUEUE_MAX_SIZE - студент не будет добавлен.

        :param username: Настоящее имя студента
        :param displayed_username: Отображаемое имя студента
        :return: True - если студент был успешно добавлен
                 False - если студент не был добавлен
        """
        if Database.QUEUE_MAX_SIZE > len(self._first_queue) + len(self._second_queue):
            self._second_queue.append([username, displayed_username])
            return True
        else:
            return False

    def add_priority_student(self, username: str, displayed_username: str) -> bool:
        """Добавляет студента в приоритетную очередь.

        Если общий размер очередей превышает QUEUE_MAX_SIZE - студент не будет добавлен.

        :param username: Настоящее имя студента
        :param displayed_username: Отображаемое имя студента
        :return: True - если студент был успешно добавлен
                 False - если студент не был добавлен
        """
        if Database.QUEUE_MAX_SIZE > len(self._first_queue) + len(self._second_queue):
            self._first_queue.append([username, displayed_username])
            return True
        else:
            return False

    def __del__(self):
        self._first_queue.clear()
        self._second_queue.clear()


db = Database()


def push_back(username: str, dis_username: str) -> tuple[Optional[bool], int]:
    """
    Returns tuple:
        1 - True, if student was added
        1 - False, if student wasn't added
        1 - None, if queue is full
        2 - if 1 is None - return queue size
        2 - student's position
    """
    pos, prior_count, count = db.find_student_position(username)
    if prior_count + count >= Database.QUEUE_MAX_SIZE:
        return None, prior_count + count
    if pos == -1:
        return db.add_student(username, dis_username), prior_count + count + 1
    return False, pos


