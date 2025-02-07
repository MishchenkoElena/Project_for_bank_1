import logging
from typing import Dict, List

import pandas as pd

# Проводим настройку логера для логирования в файл (уровень DEBUG)
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("./logs/data_read.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def data_reader_csv_excel(file_name: str) -> List[Dict]:
    """Функция для считывания финансовых операций принимает путь к файлу CSV или Excel в качестве аргумента.
    Возвращает список словарей транзакций"""
    # Определяем формат файла для выбора соответствующей обработки информации.
    if file_name.endswith("csv"):
        try:
            logger.info("Программа пытается прочитать файл-csv")
            transactions_df = pd.read_csv(file_name, sep=";", decimal=",")
            logger.info("Программа формирует список транзакций из файла")
            transactions_list = transactions_df.to_dict(orient="records")
            return transactions_list
        except Exception as e:
            logger.error(f"При чтении файла произошла ошибка {e}")
    elif file_name.endswith("xlsx"):
        try:
            logger.info("Программа пытается прочитать файл-xlsx")
            transactions_df = pd.read_excel(file_name)
            logger.info("Программа формирует список транзакций из файла")
            transactions_list = transactions_df.to_dict(orient="records")
            return transactions_list
        except Exception as e:
            logger.error(f"При чтении файла произошла ошибка {e}")
    else:
        logger.error("ValueError: Неподдерживаемый формат файла")
        raise ValueError("Неподдерживаемый формат файла")
