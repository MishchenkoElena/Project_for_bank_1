import os

import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env файла


def get_currency_conversion(operation):
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и
    конвертации суммы операции в рубли. Для конвертации валюты используется Exchange Rates Data API"""

    amount = operation.get("amount")  # Получаем сумму транзакции
    currency = operation.get("code")  # Получаем валюту транзакции

    if currency == "RUB":
        return float(amount)

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}from&amount={amount}"
    headers = {"apikey": os.getenv("API_KEY")}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:  # Если запрос успешен
        return float(response.json()["result"])  # Возвращаем результат конвертации
    else:
        return float(amount)
