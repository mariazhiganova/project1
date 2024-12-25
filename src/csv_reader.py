import csv
from typing import Optional


def get_csv(csv_path: Optional[str]) -> list:
    """ """
    try:
        with open(csv_path, mode="r", encoding="utf-8") as f:
            result_dict = csv.DictReader(f, delimiter=";")

            return list(result_dict)

    except Exception:
        return []
