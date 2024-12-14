import csv
from typing import Optional


def get_csv(csv_path: Optional[str]) -> list:
    """
    Функция, для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента
    и возвращает список словарей с транзакциями.
    """
    try:
        with open(csv_path, mode="r", encoding="utf-8") as f:
            result_dict = csv.DictReader(f, delimiter=";")

            return list(result_dict)

    except Exception:
        return []


if __name__ == "__main__":
    print(get_csv("..\\data\\transactions.csv"))
