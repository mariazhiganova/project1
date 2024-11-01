def get_mask_card_number(numbers: str) -> str:
    """
    Функция, возвращающая замаскированный номер карты
    """
    return numbers[:4] + " " + numbers[4:6] + "** ****" + " " + numbers[-4:]


my_numbers = "7000792289606361"
print(get_mask_card_number(my_numbers))


def get_mask_account(numbers: str) -> str:
    """
    Функция, возвращающая замаксированный номер счета в формате ** и четырех последних цифр
    """

    return f"**{numbers[-4:]}"


my_numbers = "73654108430135874305"
print(get_mask_account(my_numbers))
