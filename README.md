# **Проект Project_for_bank**

## *Описание:*
Разработка виджетов банковских операций клиента

## *Установка:*

Для работы с проектом, необходимо:
1. Выполнить клонирование репозитория:
git clone https://github.com/MishchenkoElena/Project_for_bank

2. Установить зависимости:
pip install - r requirements.txt

## *Использование:*

***1. Функция mask_account_card***
Функция маскировки номера принимает на вход тип и номер карты или счета клиента и возвращает маску в формате:
- для карты:

XXXX XX** **** XXXX
, где 
X - это цифра номера. То есть видны первые 6 цифр и последние 4 цифры, остальные символы скрыты звездочками.
- для счета:

**XXXX
, где 
X - это цифра номера. То есть видны только последние 4 цифры номера, остальные символы скрыты звездочками. 


***2. Функция filter_by_state***

Функция фильтрует список словарей по заданному значению


***3. Функция sort_by_date***

Функция сортирует произведенные банковские операции по дате


***4. Функция filter_by_currency***

Функция принимает на вход список словарей, представляющих транзакции и возвращает итератор, который поочередно 
выдает транзакции, где валюта операции соответствует заданной.

***5. Генератор transaction_descriptions***

Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди

***6.  Генератор card_number_generator***

Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X - цифра номера карты. 
Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
Генератор принимает начальное и конечное значения для генерации диапазона номеров.

***7. Декоратор log***

Декоратор может логировать работу функции и ее результат как в файл, так и в консоль.
Декоратор принимает необязательный аргумент filename, который определяет имя файла, в который будут записываться логи.
Если filename не задан, то логи выводятся в консоль.
Если вызов функции закончился ошибкой, записывается сообщение об ошибке и входные параметры функции.

***8. Функция get_json_operation***

Функция принимает на вход путь до JSON - файла и возвращает список словарей с данными о финансовых транзакциях. 
Если файл пустой, содержит не список или не найден, функция возвращает пустой список.

***9. Функция get_currency_conversion***

Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float. Если 
транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и конвертации 
суммы операции в рубли. Для конвертации валюты используется Exchange Rates Data API: 
https://apilayer.com/exchangerates_data-api.


***10. Функции data_read_csv и data_read_excel***

Функции для считывания финансовых операций принимает путь к файлу CSV или Excel в качестве аргумента. Возвращает 
список словарей транзакций

## *Примеры использования:*

**1. Функция маскировки номера карты или счета:**

-Пример для карты:

*Вход:*

Visa Platinum 7000792289606361

*Выход:*

Visa Platinum 7000 79** **** 6361

-Пример для счета:

*Вход:*

Счет 73654108430135874305

*Выход:*

Счет **4305

**2. Функция по фильтрации банковских операций:**

*Вход:*

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 
'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}] 

*Выход:*
- Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

- Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

**3. Функция сортировки по дате операции:** 

*Вход:*

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 
'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}] 

*Выход:*

Сортировка по убыванию, т. е. сначала самые последние операции

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

**4. Функция filter_by_currency - фильтрации операций по указанному значению валюты**

Например, для операций в валюте USD:

*Вход*

transactions = [
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
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
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

*Выход:* 

{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
}
{
          "id": 142264268,
          "state": "EXECUTED",
          "date": "2019-04-04T23:20:05.206878",
          "operationAmount": {
              "amount": "79114.93",
              "currency": {
                  "name": "USD",
                  "code": "USD" 
              }
          },
          "description": "Перевод со счета на счет",
          "from": "Счет 19708645243227258542",
          "to": "Счет 75651667383060284188"
}

**5. Генератор transaction_descriptions - для вывода типа каждой операции**

*Вход*

transactions = [
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
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
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



*Выход:* 

    Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации

**6. Генератор card_number_generator - для генерации номеров карт**

Генерация 16-ти значных номеров карт с 1 по 5

*Выход:*  

    0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005



**7. Декоратор log - для логирования выполнения функций**

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

*Ожидаемый вывод в лог-файл mylog.txt* 

- при успешном выполнении:

my_function ok

- при ошибке:

my_function error: тип ошибки. Inputs: (1, 2), {}

Где тип ошибки заменяется на текст ошибки.

**8. Функция get_json_operation**

*Вход:*  
Данные из JSON-файла в формате:
[
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  ]

*Выход:* 

[{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.
58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 
1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 41428829, 'state': 'EXECUTED', 'date': 
'2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 
'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}]

**9. Функция get_currency_conversion**

*Вход:*  

{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.
58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 
1596837868705199', 'to': 'Счет 64686473678894779589'}

*Выход:* 

31957.58


**10. Функции data_read_csv и data_read_excel**

*Вход:* 

Файл CSV содержит следующую информацию о транзакциях:
id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397; Перевод 
организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643; Перевод с 
карты на карту

*Выход:*

[
            {
                "id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210.0,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            },
            {
                "id": 3598919.0,
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "amount": 29740.0,
                "currency_name": "Peso",
                "currency_code": "COP",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
                "description": "Перевод с карты на карту",
            }
        ]

## *Тестирование:*

Для проверки корректности использования данных функций добавлены модули с тестами:

**1. tests/test_masks.py** 

Проверка корректности ввода данных карты и счета (пустой ввод или значение, отличное от 
требуемого формата данных) для функций get_mask_card_number и get_mask_account

**2. tests/test_widget.py**

Проверка корректности ввода данных карты и счета (пустой ввод или значение, отличное от 
требуемого формата данных) для функции mask_account_card, а также корректности преобразования даты в требуемый 
   формат для функции get_date. 

**3. tests/test_processing.py**

Проверка сортировки данных в зависимости от выбора значения для сортировки данных для 
функции filter_by_state, а также сортировки данных в зависимости от выбора порядка сортировки по 
дате для функции sort_by_date 

**4. tests/test_generators**

Проверка корректности фильтрации транзакций в указанной валюте для функции filter_by_currency; 
вывода информации по типам операций для функции transaction_descriptions; генерации номеров карт в соответствии с 
указанным диапазоном для функции card_number_generator

**5. tests/test_decorators**

Проверка функциональности декоратора, включая успешное выполнение функций и обработку исключений.

**6. tests/test_utils**

Проверка работы функции для получения корректных данных, в том числе в случае отсутствия файла с исходными данными, 
некорректного JSON-файла 

**7. tests/test_external_api**

Проверка корректности вывода конвертируемых данных о сумме транзакции 

**8. tests/test_data_read**

Проверка корректного считывания файлов в форматах csv и excel, а также выброса ошибки в случае отсутствия файла
