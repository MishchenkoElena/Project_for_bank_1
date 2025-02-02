from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_accounting: str) -> str:
    """Маскировка номера банковской карты или счета"""
    if not user_accounting:
        raise ValueError("Данные отсутствуют")
    else:
        user_accounting_number = "".join(symbol if symbol.isdigit() else "" for symbol in user_accounting)
        if user_accounting.lower().startswith("счет"):
            return f"Счет {get_mask_account(user_accounting_number)}"

        return f"{user_accounting[:-len(user_accounting_number)]}{get_mask_card_number(user_accounting[-len(
            user_accounting_number):])}"


def get_date(user_login_date: str) -> str:
    """Преобразование даты"""
    return f"{user_login_date[8:10]}.{user_login_date[5:7]}.{user_login_date[0:4]}"
