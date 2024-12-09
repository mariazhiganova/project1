import json
from typing import Optional


def get_transaction_data(json_file: Optional[str] = None) -> list:
    """
    Функция, которая принимает путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        if json_file is not None:
            with open(json_file, "r", encoding="utf-8") as f:
                transactions_list = json.load(f)
                if isinstance(transactions_list, list):

                    return transactions_list

        return []

    except json.JSONDecodeError:
        return []

    except FileNotFoundError:
        return []


if __name__ == "__main__":
    print(get_transaction_data("C:/Users/user/my_proj/my_project1/data/operations.json"))
