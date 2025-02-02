import pytest

from src.decorators import log


def test_log_positive(capsys):
    """Тестирует успешное выполнение декорированной функции"""

    @log()
    def function(x, y):
        return x + y


def test_log_negative(capsys):
    """Тестирует выполнение декорированной функции c ошибкой"""

    @log()
    def error_function(x, y):
        return x / y


def test_log_error(capsys):
    """Тестирует запись в консоль после ошибки"""

    @log()
    def function(x="4", y=[1, 2, 3]):
        raise ValueError("Данные введены некорректно")

    with pytest.raises(Exception):
        captured = capsys.readouterr()
        assert captured.out == "function error: TypeError. Inputs:{4}, {[1, 2, 3]}"


def test_log_good_file(capsys):
    """Тестирует запись в файл после успешного выполнения"""

    @log(filename="mylog.txt")
    def function(x, y):
        return x + y

    function(1, 2)
    assert 3
    with open("logs/mylog.txt", "r") as file:
        assert ("function called at" in line for line in file.readlines())


def test_log_exception_file(capsys):
    """Тестирует запись в файл после ошибки"""

    @log(filename="mylog.txt")
    def error_function(x, y):
        with pytest.raises(ZeroDivisionError):
            error_function(1, 0)
        with open("logs/mylog.txt", "r") as file:
            assert ("error_function error: ZeroDivisionError. Inputs:{1}, {0}" in line for line in file.readlines())
