import pytest


@pytest.fixture
def card_number():
    return "7865478076550975"


@pytest.fixture
def account_number():
    return "64756473895647563987"


@pytest.fixture
def account_num_invalid():
    return "Счет № 11111222223333344444"


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def date_invalid():
    return "2024.03.12T02:26:18.671407"


@pytest.fixture
def list_():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_2():
    return [
        {"id": 11111111, "state": "NONE", "date": "2019-07-03T18:35:29.512364"},
        {"id": 22222222, "state": "NONE", "date": "2018-06-30T02:08:58.425572"},
        {"id": 33333333, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 44444444, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def random_list():
    return [
        {"id": 11111111, "state": "NONE", "date": "2024-07-03T18:35:29.512364"},
        {"id": 22222222, "state": "CANCELED", "date": "1999-02-02T08:21:33.419442"},
        {"id": 33333333, "state": "CANCELED", "date": "2000-02-02T08:21:33.419441"},
        {"id": 44444444, "state": "NONE", "date": "2018-06-15T02:08:58.425572"},
        {"id": 55555555, "state": "CANCELED", "date": "2018-06-14T08:21:33.419443"},
    ]


@pytest.fixture
def transactions_list():
    return [
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
            "description": "Перевод со счета на счет",
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
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def transactions_list_invalid():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "GBP", "code": "GBP"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "GBP"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "RUB", "code": "RUB"}},
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


@pytest.fixture
def transactions_list_empty():
    return []


@pytest.fixture
def transaction_for_conversion():
    return {
        "id": 361044570,
        "state": "EXECUTED",
        "date": "2018-03-02T02:03:11.563721",
        "operationAmount": {"amount": "5", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 96008924215040031147",
        "to": "Счет 30377212495530283001",
    }


@pytest.fixture
def result_of_conversion():
    return """{
  "date": "2018-02-22",
  "historical": "",
  "info": {
    "rate": 148.972231,
    "timestamp": 1519328414
  },
  "query": {
    "amount": 25,
    "from": "USD",
    "to": "RUB"
  },
  "result": 531.307615,
  "success": true
}"""


@pytest.fixture
def result_of_conversion_without_result():
    return """{
  "date": "2018-02-22",
  "historical": "",
  "info": {
    "rate": 148.972231,
    "timestamp": 1519328414
  },
  "query": {
    "amount": 25,
    "from": "USD",
    "to": "RUB"
  },
  "success": true
}"""


@pytest.fixture
def transaction_for_conversion_invalid():
    return {
        "id": 361044570,
        "state": "EXECUTED",
        "date": "2018-03-02T02:03:11.563721",
        "operationAmount": {
            "amount": "5",
        },
        "description": "Перевод организации",
        "from": "Счет 96008924215040031147",
        "to": "Счет 30377212495530283001",
    }


@pytest.fixture
def csv_data_result():
    return [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]


@pytest.fixture
def excel_data():
    return {
        "id": [650703, 3598919],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z;16210", "2020-12-06T23:00:58Z;29740"],
        "amount": ["Sol", "PEN"],
    }


@pytest.fixture
def excel_data_result():
    return [
        {"id": 650703, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z;16210", "amount": "Sol"},
        {"id": 3598919, "state": "EXECUTED", "date": "2020-12-06T23:00:58Z;29740", "amount": "PEN"},
    ]


@pytest.fixture
def excel_data_invalid():
    return [1, 2, 3]
