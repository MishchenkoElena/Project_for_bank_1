import logging
import re
from collections import Counter

# Проводим настройку логера для логирования в файл (уровень INFO)
logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("../logs/sorting_data.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def filter_transactions(transactions: list[dict], search_string: str) -> list[dict]:
    """Функция для поиска в списке словарей операций по заданной строке. Принимает два аргумента: список с
    транзакциями и строку для поиска и возвращает список словарей с операциями, у которых в описании есть строка,
    переданная аргументу функции"""

    logger.info(f"Попытка фильтрации транзакций по строке: {search_string}")
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)  # Компилируем шаблон. Регистр не влияет на
    # результат поиска.
    filtered_transactions = [
        transaction for transaction in transactions if pattern.search(transaction.get("description", ""))
    ]
    logger.info(f"Найдено {len(filtered_transactions)} транзакций, соответствующих строке: {search_string}")
    return filtered_transactions


def count_transactions_by_category(transactions: list[dict], categories: list[str]) -> dict[str, int]:
    """Функция для подсчета количества банковских операций определенного типа. Принимает два аргумента: список с
    транзакциями и словарь для подсчета транзакций по описанию. Возвращает словарь, в котором ключи — это названия
    категорий, а значения — это количество операций в каждой категории"""

    logger.info("Подсчет количества транзакций по категориям")

    category_list = []
    for transaction in transactions:
        for category in categories:
            pattern = rf"{category}"
            if re.findall(pattern, transaction.get("description", ""), flags=re.IGNORECASE):
                category_list.append(transaction["description"])
    category_count = Counter(category_list)
    return dict(category_count)
