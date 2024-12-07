import json
from unittest.mock import Mock, patch

import pytest

from src.external_api import get_amount


@patch("requests.get")
def test_get_amount(mock_get, transaction_for_conversion, result_of_conversion):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = json.loads(result_of_conversion)

    result = get_amount(transaction_for_conversion)
    assert result == 531.307615


@patch("requests.get")
def test_get_amount_bad_status_code(mock_get, transaction_for_conversion, result_of_conversion):
    mock_response = Mock()
    mock_response.return_value.status_code = 404
    mock_response.reason = "Not Found"
    mock_response.return_value.json.return_value = json.loads(result_of_conversion)

    mock_get.return_value = mock_response

    with pytest.raises(Exception) as exc_info:
        get_amount(transaction_for_conversion)

    assert str(exc_info.value) == f"Запрос не был успешным. Возможная причина: {mock_response.reason}"


def test_get_amount_with_rub(transactions_list):
    result = get_amount(transactions_list[2])

    assert result == 43318.34


@patch("requests.get")
def test_get_amount_invalid_result(mock_get, transaction_for_conversion, result_of_conversion_without_result):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = json.loads(result_of_conversion_without_result)

    with pytest.raises(ValueError) as exc_info:
        get_amount(transaction_for_conversion)

        assert str(exc_info.value) == "Недостаточно данных для конвертации"


@patch("requests.get")
def test_get_amount_with_key_error(mock_get, transaction_for_conversion_invalid):
    with pytest.raises(KeyError) as exc_info:
        get_amount(transaction_for_conversion_invalid)

        assert str(exc_info.value) == "Не найдены необходимые данные для конвертации"
