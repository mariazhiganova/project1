from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(card_info: str) -> str:
    """
    Функция, возвращающая замаскированный номер карты или счета
    """
    info_list = card_info.split(" ")
    if info_list[0] == "Счет":


        return f'Счет {get_mask_account(info_list[1])}'

    else:


        return f'{info_list[0]} {info_list[1]} {get_mask_card_number(info_list[2])}'

def get_date(date: str) -> str:
    date_part = date.split("T")[0]
    year = date_part.split("-")[0]
    month = date_part.split("-")[1]
    day = date_part.split("-")[2]
    return f'{day}.{month}.{year}'

