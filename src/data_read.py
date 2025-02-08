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


def data_read_csv(csv_file_path: str) -> List[Dict]:
    """Функция для считывания финансовых операций принимает путь к файлу CSV в качестве аргумента.
    Возвращает список словарей транзакций"""
    logger.info(f"Попытка прочитать данные из CSV файла: {csv_file_path}")
    try:
        df = pd.read_csv(csv_file_path, sep=";", decimal=",")
        transactions = df.to_dict(orient="records")
        logger.info(f"Успешно считано {len(transactions)} транзакций из файла: {csv_file_path}")
        return transactions
    except Exception as e:
        logger.error(f"При чтении файла произошла ошибка: {type(e).__name__}, {e}")
        raise

def data_read_excel(excel_file_path: str) -> List[Dict]:
    """Функция для считывания финансовых операций принимает путь к файлу EXCEL в качестве аргумента.
    Возвращает список словарей транзакций"""
    try:
        logger.info(f"Попытка прочитать данные из Excel файла: {excel_file_path}")
        df = pd.read_excel(excel_file_path)
        transactions = df.to_dict(orient="records")
        logger.info(f"Успешно считано {len(transactions)} транзакций из файла: {excel_file_path}")
        return transactions
    except Exception as e:
        logger.error(f"При чтении файла произошла ошибка: {type(e).__name__}, {e}")
        raise


if __name__ == "__main__":
    csv_file_path = "../data/transactions.csv"
    excel_file_path = "../data/transactions_excel.xlsx"
    print(data_read_csv(csv_file_path))
    print(data_read_excel(excel_file_path))
