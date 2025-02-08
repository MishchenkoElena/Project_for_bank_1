import pytest

from src.sorting_data import count_transactions_by_category, filter_transactions


def test_filter_transaction_valid(transactions):
    assert filter_transactions(transactions, "организации") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

    assert filter_transactions(transactions, "карты") == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]

    assert filter_transactions(transactions, "") == transactions


def test_filter_transaction_empty_description(transactions):
    assert filter_transactions(transactions, "закрытие") == []


def test_filter_transaction_invalid():
    with pytest.raises(TypeError):
        filter_transactions(
            [
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": 123,
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                }
            ],
            "счет",
        )

    with pytest.raises(TypeError):
        filter_transactions(
            None,
            "карт",
        )

    with pytest.raises(TypeError):
        filter_transactions(
            [
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                }
            ],
            123,
        )


def test_filter_transaction_empty_list():
    assert filter_transactions([], "организации") == []


def test_count_transactions_by_category(transactions):
    categories = ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]
    assert count_transactions_by_category(transactions, categories) == {
        "Перевод организации": 2,
        "Перевод со счета на счет": 2,
        "Перевод с карты на карту": 1,
    }


def test_count_transactions_empty(transactions):
    assert count_transactions_by_category([], ["перевод"]) == {}
    assert count_transactions_by_category(transactions, []) == {}
