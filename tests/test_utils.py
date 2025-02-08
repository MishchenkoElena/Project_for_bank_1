import unittest
from unittest.mock import mock_open, patch

from src.utils import get_json_operation


class TestUtils(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_get_json_operation_empty_file(self, mock_file):
        result = get_json_operation("data/operations.json")
        self.assertEqual(result, [])  # Проверяем, что результат пустой список

    @patch("builtins.open", new_callable=mock_open, read_data="not a json")
    def test_get_json_operation_invalid_json(self, mock_file):
        result = get_json_operation("data/operations.json")
        self.assertEqual(result, [])  # Проверяем, если некорректный JSON-файл, результат - пустой список

    @patch("builtins.open", side_effect=[FileNotFoundError])
    def test_get_json_operation_file_not_found(self, mock_file):
        result = get_json_operation("data/operations.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data='{"amount": 200, "currency": "EUR"}')
    def test_get_json_operation_not_a_list(self, mock_file):
        result = get_json_operation("data/operations.json")
        self.assertEqual(result, [])  # Проверяем, если данные не из файла, результат - пустой список

    @patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 1000, "currency": "USD"}]')
    def test_get_json_operation_valid_file(self, mock_file):
        result = get_json_operation("data/operations.json")
        self.assertEqual(len(result), 1)  # Проверяем, что загружена одна транзакция
        self.assertEqual(result[0]["amount"], 1000)  # Проверяем, что сумма транзакции равна 1000
