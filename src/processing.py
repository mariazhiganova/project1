def filter_by_state(info_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция, сортирующая списки со словарями данных по ключу 'state'
    """
    result = []
    for dict_ in info_list:
        if dict_["state"] == state:
            result.append(dict_)

    return result


def sort_by_date(info_list: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция, принимающая список словарей и возвращающая отсортированный по параметру "date" в порядке убывания список
    """
    info_list.sort(key=lambda x: x["date"], reverse=reverse)

    return info_list
