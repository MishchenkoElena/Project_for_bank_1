import unittest
from unittest.mock import mock_open, patch

from src.masks import get_mask_account, get_mask_card_number


class TestMasks(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def test_get_mask_card_number(self, mock_file):
        """Проверка корректности работы функции при корректном формате данных"""
        result = get_mask_card_number(user_card_number="6831982476737658")
        self.assertEqual(
            result, "6831 98** **** 7658"
        )  # Проверка корректности работы функции при корректном формате данных

    @patch("builtins.open", new_callable=mock_open)
    def test_invalid_card_number(self, mock_file):  # Проверка работы функции при ошибочном вводе данных
        with self.assertRaises(ValueError):
            get_mask_card_number(user_card_number="683198247673765899")

    @patch("builtins.open", new_callable=mock_open)
    def test_empty_card_number(self, mock_file):  # Проверка работы функции при ошибочном вводе данных
        with self.assertRaises(ValueError):
            get_mask_card_number(user_card_number="")

    @patch("builtins.open", new_callable=mock_open)
    def test_empty_list_card_number(self, mock_file):  # Проверка работы функции при ошибочном вводе данных
        with self.assertRaises(ValueError):
            get_mask_card_number(user_card_number="[]")

    @patch("builtins.open", new_callable=mock_open)
    def test_letters_card_number(self, mock_file):  # Проверка работы функции при ошибочном вводе данных
        with self.assertRaises(ValueError):
            get_mask_card_number(user_card_number="abcde")

    @patch("builtins.open", new_callable=mock_open)
    def test_zero_card_number(self, mock_file):  # Проверка работы функции при ошибочном вводе данных
        with self.assertRaises(ValueError):
            get_mask_card_number(user_card_number="0")

    @patch("builtins.open", new_callable=mock_open)
    def test_mask_account_number(self, mock_file):
        result = get_mask_account(user_number_account="73654108430135874305")
        self.assertEqual(result, "**4305")  # Проверка корректности работы функции при корректном формате данных

    @patch("builtins.open", new_callable=mock_open)
    def test_invalid_account_number(self, mock_file):  # Проверка работы функции при ошибочном вводе данных
        with self.assertRaises(ValueError):
            get_mask_account(user_number_account="736541084301358743")

    @patch("builtins.open", new_callable=mock_open)
    def test_empty_account_number(self, mock_file):  # Проверка работы функции при ошибочном вводе данных
        with self.assertRaises(ValueError):
            get_mask_account(user_number_account="")

    @patch("builtins.open", new_callable=mock_open)
    def test_zero_account_number(self, mock_file):  # Проверка работы функции при ошибочном вводе данных
        with self.assertRaises(ValueError):
            get_mask_account(user_number_account="0")

    @patch("builtins.open", new_callable=mock_open)
    def test_empty_list_account_number(self, mock_file):  # Проверка работы функции при ошибочном вводе данных
        with self.assertRaises(ValueError):
            get_mask_account(user_number_account="[]")

    @patch("builtins.open", new_callable=mock_open)
    def test_letters_account_number(self, mock_file):  # Проверка работы функции при ошибочном вводе данных
        with self.assertRaises(ValueError):
            get_mask_account(user_number_account="abcde")
