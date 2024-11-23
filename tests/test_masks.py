import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "7865 47** **** 0975"


@pytest.mark.parametrize(
    "card_num, mask_num",
    [
        ("1111222233334444", "1111 22** **** 4444"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("0001000200030004", "0001 00** **** 0004"),
    ],
)
def test_mask_card_use_parametrize(card_num, mask_num):
    assert get_mask_card_number(card_num) == mask_num


@pytest.mark.parametrize(
    "card_num_invalid",
    [
        ("1234"),
        (""),
        ("12345678901234567890"),
        ("123abc456def7890"),
    ],
)
def test_mask_card_number_invalid(card_num_invalid):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_num_invalid)

    assert str(exc_info.value) == "Неверный номер карты"


def test_get_mask_account_number(account_number):
    assert "**3987"


@pytest.mark.parametrize("invalid_account_num", [("123"), (""), ("12345678901234567890123"), ("account.number123456")])
def test_mask_invalid_account_num(invalid_account_num):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(invalid_account_num)

    assert str(exc_info.value) == "Неверный номер счёта"
