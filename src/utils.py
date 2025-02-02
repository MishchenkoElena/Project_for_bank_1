import json
import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

file_path = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")

logger = logging.getLogger("utils")  # Настройка логирования

# Создание хандлера для записи логов в файл
file_handler = logging.FileHandler("../logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)  # Установлен уровень логирования не ниже DEBUG

# Создание и установка форматера для записи логов в файл
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_json_operation(file_path):
    """Функция принимает на вход путь до JSON - файла и возвращает список словарей с данными о финансовых
    транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""

    try:
        with open(file_path, "r", encoding="UTF-8") as f:
            try:
                operations = json.load(f)  # Попытка загрузить транзакции из файла
                if isinstance(operations, list):  # Проверяем, являются ли загруженные данные списком
                    logger.info(f"Транзакции успешно загружены из файла: {file_path}")
                    return operations
                else:
                    logger.warning(f"Данные в файле {file_path} не являются списком.")
                    return []
            except json.JSONDecodeError as e:
                logger.error(f"Ошибка при декодировании JSON из файла {file_path}: {e}")
                return []  # Если ошибка при декодировании JSON, возвращается пустой список
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден")


if __name__ == "__main__":
    print(get_json_operation(file_path))
