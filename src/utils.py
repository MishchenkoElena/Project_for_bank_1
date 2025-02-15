import json
import logging
from typing import Dict, List, Union

logger = logging.getLogger(__file__)  # Настройка логирования

# Создание хендлера для записи логов в файл
file_handler = logging.FileHandler("../logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)  # Установлен уровень логирования не ниже DEBUG

# Создание и установка форматера для записи логов в файл
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_json_operation(file_path: str) -> List[Dict[str, Union[str, int, dict, float]]]:
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
        return []
