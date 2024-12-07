import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_amount(transaction: dict) -> float:
    """
    Функция, которая принимает на вход транзакцию
    и возвращает сумму транзакции в рублях
    """
    try:

        currency = transaction["operationAmount"]["currency"]["code"]
        amount = float(transaction["operationAmount"]["amount"])

        if currency == "RUB":

            return amount

        else:

            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

            headers = {"apikey": API_KEY}

            response = requests.get(url, headers=headers)

            status_code = response.status_code

            if status_code == 200:
                content = response.json()

                if "result" in content:

                    return float(content["result"])

                else:

                    raise ValueError("Недостаточно данных для конвертации")

            else:

                raise Exception(f"Запрос не был успешным. Возможная причина: {response.reason}")

    except KeyError:

        raise KeyError("Не найдены необходимые данные для конвертации")
