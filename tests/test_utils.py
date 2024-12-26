from unittest.mock import mock_open, patch

import pytest

from src.utils import get_transaction_data
from settings import JSON_PATH


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_get_transaction_data_valid_file(mock_file):
    transactions = get_transaction_data(JSON_PATH)

    assert transactions == [{"amount": 100, "currency": "USD"}]
    mock_file.assert_called_with(JSON_PATH, "r", encoding="utf-8")


@patch("builtins.open", side_effect=FileNotFoundError)
def test_get_transaction_data_invalid_file(mock_open):
    with pytest.raises(FileNotFoundError):
        get_transaction_data("invalid\\path")


def test_get_transaction_data_invalid_file_else():
    result = get_transaction_data("invalid\\path")
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_get_transaction_data_invalid_file_else_2(mock_file):
    transactions = get_transaction_data(JSON_PATH)

    assert transactions == []
    mock_file.assert_called_with(JSON_PATH, "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="not a json")
def test_get_transaction_data_error_file(mock_file):
    transactions = get_transaction_data(JSON_PATH)

    assert transactions == []
    mock_file.assert_called_with(JSON_PATH, "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="100")
def test_get_transaction_data_not_list(mock_file):
    transactions = get_transaction_data(JSON_PATH)

    assert transactions == []
    mock_file.assert_called_with(JSON_PATH, "r", encoding="utf-8")
