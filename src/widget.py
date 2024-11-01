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
