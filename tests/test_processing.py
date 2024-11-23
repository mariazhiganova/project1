from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_use_parametrize(random_list):
    assert filter_by_state(random_list) == []


def test_filter_by_state(list_):
    assert filter_by_state(list_, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_else(list_):
    assert filter_by_state(list_) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_invalid(list_2):
    assert filter_by_state(list_2) == []


def test_sort_by_date(random_list):
    assert sort_by_date(random_list) == [
        {"id": 11111111, "state": "NONE", "date": "2024-07-03T18:35:29.512364"},
        {"id": 44444444, "state": "NONE", "date": "2018-06-15T02:08:58.425572"},
        {"id": 55555555, "state": "CANCELED", "date": "2018-06-14T08:21:33.419443"},
        {"id": 33333333, "state": "CANCELED", "date": "2000-02-02T08:21:33.419441"},
        {"id": 22222222, "state": "CANCELED", "date": "1999-02-02T08:21:33.419442"},
    ]
