import re
from typing import List


def get_searched_transactions(transactions: list, search_str: str) -> List[dict]:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)

    result = []

    for transaction in transactions:

        if "description" in transaction and search_str:
            if re.search(pattern, transaction["description"]):
                result.append(transaction)

        else:
            return []

    return result


def get_transactions_count_by_category(transactions: list, category_list: list) -> dict:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, где ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    result = {}

    if category_list:

        for category in category_list:

            pattern = re.compile(re.escape(category), flags=re.IGNORECASE)

            counter = 0

            for transaction in transactions:

                if re.search(pattern, transaction["description"]):
                    counter += 1

                    result[category] = counter

    else:
        raise Exception("Список категорий пуст")

    return result
