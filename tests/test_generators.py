import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions_list, currency="USD"):
    gen = filter_by_currency(transactions_list, "USD")
    assert next(gen) == {
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
    assert next(gen) == {
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


def test_filter_by_invalid_currency(transactions_list_invalid, currency="USD"):
    gen = filter_by_currency(transactions_list_invalid, "USD")
    assert next(gen) == "Операции в заданной валюте не найдены"


def test_filter_by_invalid_currency_empty(transactions_list_empty, currency="USD"):
    gen = filter_by_currency(transactions_list_empty, "USD")
    assert next(gen) == "Операции в заданной валюте не найдены"


def test_transaction_descriptions(transactions_list):
    gen = transaction_descriptions(transactions_list)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"


def test_transaction_descriptions_empty(transactions_list_empty):
    gen = transaction_descriptions(transactions_list_empty)
    assert next(gen) == "Нет транзакций"


def test_card_number_generator():
    number = card_number_generator(1, 11)
    assert next(number) == "0000 0000 0000 0001"
    assert next(number) == "0000 0000 0000 0002"
    assert next(number) == "0000 0000 0000 0003"
    assert next(number) == "0000 0000 0000 0004"
    assert next(number) == "0000 0000 0000 0005"
    assert next(number) == "0000 0000 0000 0006"
    assert next(number) == "0000 0000 0000 0007"
    assert next(number) == "0000 0000 0000 0008"
    assert next(number) == "0000 0000 0000 0009"
    assert next(number) == "0000 0000 0000 0010"
    assert next(number) == "0000 0000 0000 0011"


def test_card_number_generator_finally():
    number = card_number_generator(9999999999999998, 9999999999999999)
    assert next(number) == "9999 9999 9999 9998"
    assert next(number) == "9999 9999 9999 9999"


def test_card_number_generator_finally_else():
    number = card_number_generator(9999999999999999, 10000000000000000000)
    assert next(number) == "9999 9999 9999 9999"
