def filter_by_currency(transactions, cod_currency):
    """Функция принимает на вход список словарей, представляющих транзакции и возвращает итератор, который поочередно
    выдает транзакции, где валюта операции соответствует заданной"""
    return (
        transaction
        for transaction in transactions
        if transaction["operationAmount"]["currency"]["code"] == cod_currency
    )


def transaction_descriptions(transactions):
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    description_transaction = (transaction.get("description") for transaction in transactions)
    for x in description_transaction:
        if x != "":
            yield x


def card_number_generator(start, stop):
    """Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X - цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор принимает начальное и конечное значения для генерации диапазона номеров"""
    for number in range(start, stop):
        yield (
            f"{str(number).zfill(16)[:4]} {str(number).zfill(16)[4:8]} {str(number).zfill(16)[8:12]}"
            f" {str(number).zfill(16)[12:]}"
        )
