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
