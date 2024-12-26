def filter_by_currency(info_list, currency):
    """
    Функция, находящая операции в заданной валюте
    """
    if not info_list:
        raise ValueError("Список транзакций пуст")

    for transaction in info_list:
        if "operationAmount" in transaction:
            result_by_currency = (x for x in info_list if x["operationAmount"]["currency"]["code"] == currency)
            first_item = next(result_by_currency, None)

            if first_item is None:
                raise ValueError("Операции в заданной валюте не найдены")

            yield first_item
            yield from result_by_currency

        elif "currency_code" in transaction:
            result_by_currency = (x for x in info_list if x["currency_code"] == currency)
            first_item = next(result_by_currency, None)

            if first_item is None:
                raise ValueError("Операции в заданной валюте не найдены")

            yield first_item
            yield from result_by_currency

        else:
            raise KeyError("Информация о валюте отсутствует")


def transaction_descriptions(info_list):
    """
    Функция, выводящая описания операций из списка
    """
    if len(info_list) == 0:
        return []

    for x in info_list:
        yield x["description"]


def card_number_generator(start, stop):
    """
    Функция, генерирующая номера банковских карт в заданном 16-значном формате
    """
    if start > stop:

        raise ValueError("Ошибка: Start не должен превышать Stop")

    else:

        for number in range(start, stop + 1):

            number_str = str(number)

            if len(str(number)) < 16:
                card_number_not_formatted = "0" * (16 - len(str(number))) + str(number)
            else:
                card_number_not_formatted = number_str

            card_number = f"{card_number_not_formatted[:4]} {card_number_not_formatted[4:8]} {card_number_not_formatted[8:12]} {card_number_not_formatted[12:]}"

            yield card_number
