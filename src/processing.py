def filter_by_state(list_of_dictionaries: list, state: str = "EXECUTED") -> list:
    """
        Функция принимает список словарей и опционально значение для ключа state (по умолчанию
    'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению
    """

    new_list_of_dictionaries = []
    for dictionary in list_of_dictionaries:
        if dictionary.get("state") == state:
            new_list_of_dictionaries.append(dictionary)
    return new_list_of_dictionaries


def sort_by_date(list_of_dictionaries: list, sort_order: bool = True) -> list:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию —
    убывание) и возвращает новый список, отсортированный по дате (date)
    """
    sorted_list_of_dictionaries = sorted(
        list_of_dictionaries, key=lambda dictionary: dictionary["date"], reverse=sort_order
    )
    return sorted_list_of_dictionaries
