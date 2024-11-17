import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_or_account, expected_value",
    [
        ("Счет 57687987545678904567", "Счет **4567"),
        ("Visa Super 6576863456789043", "Visa Super 6576 86** **** 9043"),
        ("MasterCard 7688743334445556", "MasterCard 7688 74** **** 5556"),
        ("Visa Super Puper Figuper 7654333444000999", "Visa Super Puper Figuper 7654 33** **** 0999"),
    ],
)
def test_mask_account_card(card_or_account, expected_value):
    assert mask_account_card(card_or_account) == expected_value


def test_mask_account_invalid(account_num_invalid):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(account_num_invalid)

    assert str(exc_info.value) == "Неверный номер счёта"


def test_get_date(date):
    assert get_date(date) == "11.03.2024"


def test_get_date_invalid(date_invalid):
    with pytest.raises(ValueError) as exc_info:
        get_date(date_invalid)

    assert str(exc_info.value) == "Неверный формат даты"


@pytest.mark.parametrize(
    "dates_invalid",
    [
        ("2024-13-12T02:26:18.671407"),
        ("2024-03-32T02:26:18.671407"),
    ],
)
def test_get_date_invalid_else(dates_invalid):
    with pytest.raises(ValueError) as exc_info:
        get_date(dates_invalid)

    assert str(exc_info.value) == "Неверная дата"

