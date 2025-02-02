import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_usd_currency(transactions, cod_currency="USD"):
    """Проверка корректности фильтрации транзакций в указанной валюте"""
    generator_usd = filter_by_currency(transactions, cod_currency)
    assert next(generator_usd) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_filter_empty_list(transactions):
    """Проверка корректности в случае отсутствия данных по транзакциям"""
    transaction_list_empty = []
    result = list(filter_by_currency(transaction_list_empty, "USD"))
    assert result == []


def test_filter_by_currency_non_existent(transactions):
    """Проверка корректности в случае отсутствия транзакций в указанной валюте"""
    transact_non_code_currency = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]

    result = list(filter_by_currency(transact_non_code_currency, "USD"))
    assert result == []


def test_transaction_empty_descriptions(transactions):
    """Проверка корректности вывода информации при отсутствии данных по типу операции"""
    empty_descriptions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]

    result = list(transaction_descriptions(empty_descriptions))
    assert result == ["Перевод со счета на счет"]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1234567812345678, 1234567812345679, "1234 5678 1234 5678"),
        (1234123412341231, 1234123412341232, "1234 1234 1234 1231"),
        (4998765432567890, 4998765432567891, "4998 7654 3256 7890"),
    ],
)
def test_card_number_generator(start, stop, expected):
    """Проверка корректности генерации номеров карт"""
    generator = card_number_generator(start, stop)
    assert next(generator) == expected
