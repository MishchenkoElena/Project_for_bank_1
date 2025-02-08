from src.data_read import data_read_csv, data_read_excel
from src.processing import filter_by_state, sort_by_date
from src.sorting_data import filter_transactions
from src.utils import get_json_operation
from src.widget import get_date, mask_account_card


def main():
    """Функция отвечает за основную логику проекта и связывает функциональности между собой"""
    # Приветствие пользователя и начало работы

    global transactions_list
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор источника информации
    while True:
        choice = input(
            """Выберите необходимый пункт меню (1, 2, 3)
        1 - Получить информацию о транзакциях из JSON-файла
        2 - Получить информацию о транзакциях из CSV-файла
        3 - Получить информацию о транзакциях из XLSX-файла\n"""
        )
        if choice in ("1", "2", "3"):
            break
        else:
            print("Введен некорректный ответ. Повторите ввод")

    menu = {
        "1": "Для обработки выбран JSON-файл",
        "2": "Для обработки выбран CSV-файл",
        "3": "Для обработки выбран XLSX-файл",
    }
    print(f"{menu[choice]}")

    if choice == "1":
        transactions_list = get_json_operation("./data/operations.json")
    elif choice == "2":
        transactions_list = data_read_csv("./data/transactions.csv")
    elif choice == "3":
        transactions_list = data_read_excel("./data/transactions_excel.xlsx")

    # Фильтрация по статусу операций
    while True:
        valid_status = {"1": "EXECUTED", "2": "CANCELED", "3": "PENDING"}
        status = (
            input(
                """Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы:
        1 - EXECUTED
        2 - CANCELED
        3 - PENDING\n"""
            )
            .strip()
            .upper()
        )
        if status in valid_status:
            break
        else:
            print("Введен некорректный ответ. Повторите ввод")

    filtered_transactions = filter_by_state(transactions_list, valid_status[status])
    print(f"Операции отфильтрованы по статусу {valid_status[status]}")

    # Дополнительные фильтры
    choice_date_sort = input("Отфильтровать операции по дате? Да/Нет\n").strip().lower()
    if choice_date_sort in ("да", "нет"):
        if choice_date_sort == "да":
            order_map = {"1": False, "2": True}
            choice_sort_order = input(
                """Отфильтровать транзакции по возрастанию или убыванию?
        1 - по возрастанию
        2 - по убыванию\n"""
            ).strip()
            if choice_sort_order in order_map:
                date_sorted_transactions = sort_by_date(filtered_transactions, order_map[choice_sort_order])
            else:
                print("Введен некорректный ответ. Повторите ввод")
        elif choice_date_sort == "нет":
            date_sorted_transactions = filtered_transactions
    else:
        print("Введен некорректный ответ. Повторите ввод")

    # Фильтрация по валюте
    choice_rub = (
        input(
            """Выводить только рублевые транзакции?
        Да/Нет\n"""
        )
        .strip()
        .lower()
    )
    if choice_rub == "да":
        if choice == "1":
            transactions_currency = list(
                transaction
                for transaction in date_sorted_transactions
                if transaction["operationAmount"]["currency"]["code"] == "RUB"
            )
        elif choice in ("2", "3"):
            transactions_currency = list(
                transaction for transaction in date_sorted_transactions if transaction["currency_code"] == "RUB"
            )
    elif choice_rub == "нет":
        transactions_currency = date_sorted_transactions
    else:
        print("Введен некорректный ответ. Повторите ввод")

    # Фильтрация по определенному слову в описании
    description_filter = (
        input(
            """Отфильтровать список транзакций по определенному слову в описании?
        Да/Нет\n"""
        )
        .strip()
        .lower()
    )
    if description_filter == "да":
        search_word = input("""Введите слово для поиска в описании\n""")
        filtered_transactions_final = filter_transactions(transactions_currency, search_word)
    elif description_filter == "нет":
        filtered_transactions_final = transactions_currency
    else:
        print("Введен некорректный ответ. Повторите ввод")

    # Вывод результатов
    if filtered_transactions_final:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions_final)}")

        for transaction in filtered_transactions_final:
            if choice == "1":
                summa_print = transaction["operationAmount"]["amount"]
                currency_print = transaction["operationAmount"]["currency"]["code"]
            elif choice in ("2", "3"):
                summa_print = transaction["amount"]
                currency_print = transaction["currency_code"]
            date_print = get_date(transaction["date"])
            description_print = transaction["description"]
            to_print = mask_account_card(transaction["to"])

            if transaction["description"] == "Открытие вклада":
                print(
                    f"""
        {date_print} {description_print}
        {to_print} Сумма:{summa_print} {currency_print}\n"""
                )
            else:
                from_print = mask_account_card(transaction["from"])
                print(
                    f"""
        {date_print} {description_print}
        {from_print} -> {to_print}
        Сумма: {summa_print} {currency_print}\n"""
                )

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
