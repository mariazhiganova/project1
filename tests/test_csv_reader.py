from unittest.mock import mock_open, patch
from src.csv_reader import get_csv


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n"
    "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;"
    "Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n"
    "3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;"
    "Discover 0720428384694643; Перевод с карты на карту",
)
def test_csv_reader(mock_file, csv_data_result):
    transactions = get_csv("data/transactions.csv")

    assert transactions == csv_data_result
    mock_file.assert_called_once_with("data/transactions.csv", mode="r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_csv_invalid(mock_file):
    transactions = get_csv("data/transactions.csv")

    assert transactions == []
    mock_file.assert_called_once_with("data/transactions.csv", mode="r", encoding="utf-8")


def test_read_csv_invalid_path():
    transactions = get_csv("some/invalid/path")

    assert transactions == []


def test_read_csv_not_path():
    transactions = get_csv("")

    assert transactions == []
