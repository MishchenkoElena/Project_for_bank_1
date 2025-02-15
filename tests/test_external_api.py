import unittest
from unittest.mock import patch

from src.external_api import get_currency_conversion


class TestUtils(unittest.TestCase):

    @patch("requests.get")
    def test_get_currency_conversion_rub(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 1000}  # Симулируем ответ API

        operation = {"amount": 1000, "currency": "RUB"}  # Тестовая транзакция
        result = get_currency_conversion(operation)
        self.assertEqual(result, 1000.0)  # Проверяем, что возвращается значение в рублях из транзакции

    @patch("requests.get")
    def test_get_currency_conversion_from_USD(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 9200}  # Симулируем ответ API

        operation = {"amount": 100, "currency": "USD"}  # Тестовая транзакция в долларах
        result = get_currency_conversion(operation)
        self.assertEqual(result, 9200.0)  # Проверяем, что результат конвертации в рубли равен 9200
