import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "user_account, mask_account",
    [
        ("Visa 6831982476737658", "Visa 6831 98** **** 7658"),
        ("Master Card 6831982476737658", "Master Card 6831 98** **** " "7658"),
        ("счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(user_account: str, mask_account: str) -> None:
    assert mask_account_card(user_account) == mask_account


def test_invalid_account_card(user_account: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card("Master 683198247673765" "Visa 68319824767376587" "0" "" "[]")


@pytest.mark.parametrize(
    "date, correct_date", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-03-11", "11.03.2024")]
)
def test_get_date(date: str, correct_date: str) -> None:
    assert get_date(date) == correct_date
