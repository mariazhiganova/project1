import pytest

from src.transactions_filter import get_searched_transactions, get_transactions_count_by_category


def test_get_searched_transactions(transactions_list, result_transactions_filter):
    result = get_searched_transactions(transactions_list, "Счет")

    assert result == result_transactions_filter


def test_get_searched_transaction_empty_list(transactions_list_empty):
    result = get_searched_transactions(transactions_list_empty, "Счет")

    assert result == []


def test_get_searched_transaction_empty_search(transactions_list):
    result = get_searched_transactions(transactions_list, "")

    assert result == []


def test_get_searched_transaction_invalid_search(transactions_list):
    result = get_searched_transactions(transactions_list, "приветик!")

    assert result == []


def test_get_searched_transaction_without_transactions(random_list):
    result = get_searched_transactions(random_list, "пупупу")

    assert result == []


def test_get_transactions_count_by_category(transactions_list, category_list):
    result = get_transactions_count_by_category(transactions_list, category_list)

    assert result == {"Перевод организации": 2, "Перевод с карты на карту": 1, "Перевод со счета на счет": 2}


def test_get_transactions_count(transactions_list_empty, category_list):
    result = get_transactions_count_by_category(transactions_list_empty, category_list)

    assert result == {}


def test_get_transactions_without_category(transactions_list):
    with pytest.raises(Exception) as exc_info:
        get_transactions_count_by_category(transactions_list, [])

    assert exc_info.value.args[0] == "Список категорий пуст"
