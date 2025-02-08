import unittest
from unittest.mock import patch

import pytest

from src.data_read import data_reader_csv_excel


class TestUtils(unittest.TestCase):
    # Тестирование считывания файла-csv

    @patch("pandas.read_csv")
    def test_csv_reader(self, mock_read_csv):
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
        result = data_reader_csv_excel("./data/transaction.csv")
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
    def test_excel_reader(self, mock_read_excel):
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
        result = data_reader_csv_excel("./data/transaction_excel.xlsx")
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

    # Тестирование ошибок
    # Неподдерживаемый формат файла
    def test_csv_excel_reader_with_wrong_format_file(self):
        with pytest.raises(ValueError) as exc_info:
            data_reader_csv_excel("file.txt")
            assert str(exc_info.value) == "Неподдерживаемый формат файла"

        # Ошибка при считывании информации при отсутствии файла

    # Ошибка при считывании файла
    def test_csv_excel_reader_wrong_file(self):
        with pytest.raises(Exception) as exc_info:
            data_reader_csv_excel("file_none.csv")
            assert str(exc_info.value) == "При чтении файла произошла ошибка"
