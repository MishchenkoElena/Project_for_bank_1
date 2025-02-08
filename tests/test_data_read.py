import unittest
from unittest.mock import patch

import pytest

from src.data_read import data_read_csv, data_read_excel


class TestUtils(unittest.TestCase):
    # Тестирование считывания файла-csv

    @patch("pandas.read_csv")
    def test_data_read_csv(self, mock_read_csv):
        mock_read_csv.return_value.to_dict.return_value = [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        result = data_read_csv("data/transactions.csv")
        assert result == [
            {
                "id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210.0,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]

    # Тестирование считывания файла-xlsx
    @patch("pandas.read_excel")
    def test_data_read_excel(self, mock_read_excel):
        mock_read_excel.return_value.to_dict.return_value = [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        result = data_read_excel("data/transactions_excel.xlsx")
        assert result == [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]

    # Ошибка при считывании информации при отсутствии файла
    def test_file_not_found_csv(self):
        """Тестирование обработки ошибки при отсутствии csv-файла"""
        with patch("os.path.exists", return_value=False):  # Подмена os.path.exists
            with pytest.raises(FileNotFoundError):
                data_read_csv("")

    def test_file_not_found_excel(self):
        """Тестирование обработки ошибки при отсутствии excel-файла"""
        with patch("os.path.exists", return_value=False):  # Подмена os.path.exists
            with pytest.raises(FileNotFoundError):
                data_read_excel("")
