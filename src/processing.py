def filter_by_state(info_list: list[dict], state='EXECUTED') -> list[dict]:
    result = []
    for dict_ in info_list:
        if dict_['state'] == state:
            result.append(dict_)


    return result
