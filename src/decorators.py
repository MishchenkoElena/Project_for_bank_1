import logging
import os
from datetime import datetime


def setup_logger(filename):
    """Настройка логирования"""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(message)s")

    if filename:
        log_file = os.path.join("./logs", filename)
        os.makedirs(os.path.dirname(log_file), exist_ok=True)  # Создание папки logs
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


def log(filename=""):
    """Декоратор выполняет логирование выполнения функции, ее результаты при успешной операции или возникновении
    ошибок.
    Декоратор принимает необязательный аргумент filename, который определяет, куда будут записываться логи:
    - в файл, если filename задан;
    - в консоль, если filename не задан"""
    logger = setup_logger(filename)

    def decorator(function):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            logger.info(f"{function.__name__} started at {start_time.isoformat()}")

            try:
                result = function(*args, **kwargs)
                end_time = datetime.now()
                logger.info(f"{function.__name__} finished at {end_time.isoformat()}")
                logger.info(f"{function.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{function.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise e

        return wrapper

    return decorator
