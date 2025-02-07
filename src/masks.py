import logging
from typing import Union

logger = logging.getLogger(__file__)

# Создание хандлера для записи логов в файл
file_handler = logging.FileHandler("./logs/masks.log", mode="w")
# Настройка логирования для модуля masks
logger.setLevel(logging.DEBUG)

# Форматирование логов
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(user_card_number: Union[int, str]) -> str:
    """Маскировка номера банковской карты"""
    logger.debug(f"Получение маски для номера карты: {user_card_number}")

    if len(str(user_card_number)) != 16 or not str(user_card_number.isdigit()):
        logger.error("Ошибка: Данные введены некорректно: номер должен состоять из 16 цифр")
        raise ValueError("Данные введены некорректно: номер должен состоять из 16 цифр")
    """Маскировка номера банковского счета (видны первые 6 и последние 4 цифры, остальные замаскированы)"""
    mask_card = f"{str(user_card_number)[:4]} {str(user_card_number)[4:6]}** **** {str(user_card_number)[-4:]}"
    logger.info(f"Маска карты успешно создана: {mask_card}")
    return mask_card


def get_mask_account(user_number_account: Union[int, str]) -> str:
    """Маскировка номера банковского счета"""
    logger.debug(f"Получение маски для номера счета: {user_number_account}")
    if len(str(user_number_account)) != 20 or not str(user_number_account.isdigit()):
        logger.error("Ошибка: Данные введены некорректно: номер счета должен состоять из 20 цифр")
        raise ValueError("Данные введены некорректно: номер счета должен состоять из 20 цифр")

    mask_account = f"**{str(user_number_account)[-4:]}"
    logger.info(f"Маска счета успешно создана: {mask_account}")

    return mask_account
