from unittest.mock import patch
import pandas as pd

from src.excel_reader import get_excel


@patch("pandas.read_excel")
def test_get_excel(mock_read_excel, excel_data, excel_data_result):
    mock_read_excel.return_value = pd.DataFrame(excel_data)

    result = get_excel("..\\data\\transactions.xlsx")
    assert result == excel_data_result


def test_get_excel_no_path():
    result = get_excel("")

    assert result == []


def test_get_excel_invalid_path():
    result = get_excel("files/some_file.xlsx")

    assert result == []


@patch("pandas.read_excel")
def test_get_excel_empty(mock_read_excel):
    mock_read_excel.return_value = ""

    result = get_excel("files/some_file.xlsx")
    assert result == []
