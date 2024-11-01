def get_mask_card_number(numbers: str) -> str:
    """
    Функция, возвращающая замаскированный номер карты
    """
    return numbers[:4] + " " + numbers[4:6] + "** ****" + " " + numbers[-4:]


def get_mask_account(numbers: str) -> str:
    """
    Функция, возвращающая замаксированный номер счета в формате ** и четырех последних цифр
    """

    return f"**{numbers[-4:]}"
