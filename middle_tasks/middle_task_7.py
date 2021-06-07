# TODO: определить по коду аннотации типов для функции, параметров и переменных. Написать тесты для этой функции.

CATEGORY_TYPES = [
    'PrivilegeList',
    'System',
    'Data'
]


def set_column_value(column_categories, value, _row_values):
    """ Очищает наименование категории и стандартизирует значение ячейки категории.

    Если value имеет неожидаемый тип - бросается исключение TypeError.

    :param column_categories: список строк, содержащих названия категорий, к которым принадлежит значение value
    :param value: значение, хранящееся в ячейке
    :param _row_values: словарь отфильтрованных значений
    """
    tmp = ""

    if type(value) is str:
        value = value.strip()
    if value in ['', '-']:
        value = 0

    if type(value) is bool:
        value = int(value)

    if type(value) not in [int, str]:
        raise TypeError

    for category in column_categories:
        tmp += "-" + category

    for index in range(len(CATEGORY_TYPES)):
        if CATEGORY_TYPES[index] == column_categories[0]:
            tmp = tmp[len(CATEGORY_TYPES[index]) + 1:]
            if index == 0:
                tmp = tmp[5:]

    if tmp.endswith("-TextValue"):
        tmp = tmp[:-10]
    tmp = tmp[1:]

    assert _row_values.get(tmp) is not None
    _row_values[tmp] = value
