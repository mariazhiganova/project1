from settings import CSV_PATH, JSON_PATH, XLSX_PATH
from src.csv_reader import get_csv
from src.excel_reader import get_excel
from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.transactions_filter import get_searched_transactions
from src.utils import get_transaction_data
from src.widget import get_date, mask_account_card


def main():
    """
    Функция отвечает за основную логику проекта
    и связывает функциональности между собой.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("Выберите необходимый пункт меню:")
        print(
            "1. Получить информацию о транзакциях из JSON-файла"
            "\n2. Получить информацию о транзакциях из CSV-файла"
            "\n3. Получить информацию о транзакциях из XLSX-файла"
        )

        user_choose_point = str(input("Введите номер пункта меню (1-3): "))

        if user_choose_point == "1":
            print("Для обработки выбран JSON-файл.")
            transaction_dict = get_transaction_data(JSON_PATH)
            break

        elif user_choose_point == "2":
            print("Для обработки выбран CSV-файл.")
            transaction_dict = get_csv(CSV_PATH)
            break

        elif user_choose_point == "3":
            print("Для обработки выбран XLSX-файл.")
            transaction_dict = get_excel(XLSX_PATH)
            break

        else:
            print("Введен неверный номер пункта меню.")

    print(
        "Выберите статус, по которому необходимо выполнить фильтрацию. "
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )

    while True:
        user_choose_status = input("Введите статус: ")

        if user_choose_status.upper() in ["EXECUTED", "CANCELED", "PENDING"]:

            transactions = filter_by_state(transaction_dict, user_choose_status)
            break

        else:
            print(f"Статус операции {user_choose_status} недоступен")

    while True:
        user_choose_data_filter = input("Отсортировать операции по дате? Да/Нет: ")

        if user_choose_data_filter.title() == "Да":

            while True:
                user_choose_data_filter_reverse = input("Отсортировать по возрастанию или по убыванию? ")

                if user_choose_data_filter_reverse.lower() == "по убыванию":
                    sorted_transactions = sort_by_date(transactions)
                    break

                elif user_choose_data_filter_reverse.lower() == "по возрастанию":
                    sorted_transactions = sort_by_date(transactions, reverse=False)
                    break

                else:
                    print("Введен неверный ответ. Введите 'по возрастанию' или 'по убыванию'")

            break

        elif user_choose_data_filter.title() == "Нет":
            sorted_transactions = transactions
            break

        else:
            print("Введен неверный ответ. Введите 'Да' или 'Нет'")


    while True:
        user_choose_rub = input("Выводить только рублевые транзакции? Да/Нет: ")

        if user_choose_rub.title() == "Да":
            transactions_by_currency = list(filter_by_currency(sorted_transactions, "RUB"))
            break

        elif user_choose_rub.title() == "Нет":
            transactions_by_currency = sorted_transactions
            break

        else:
            print("Введен неверный ответ. Введите 'Да' или  'Нет'")
            continue

    print("Отфильтровать список транзакций по определенному слову в описании?")

    while True:
        user_choose_word_filter = input("Да/Нет ")

        if user_choose_word_filter.title() == "Да":
            user_search = input("Введите слово для поиска по описанию: ")
            result = list(get_searched_transactions(transactions_by_currency, user_search))
            break

        elif user_choose_word_filter.title() == "Нет":
            result = list(transactions_by_currency)

            break

        else:
            print("Введен неверный ответ. Введите 'Да' или  'Нет'")
            continue

    if result:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(result)}")

        for transaction in result:
            if "date" in transaction:

                description = next(transaction_descriptions(result), "Описание отсутствует")
                print(f'{get_date(transaction["date"])} {description}')

                if transaction.get("from") and transaction.get("from"):
                    print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")

                elif not transaction.get("from") and transaction.get("to"):
                    print(f"{mask_account_card(transaction['to'])}")

                if user_choose_point == "1":
                    print(
                        f"Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}\n"
                    )

                elif user_choose_point == "2" or user_choose_point == "3":
                    print(f"Сумма: {transaction['amount']} {transaction['currency_name']}\n")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    return result


if __name__ == "__main__":
    main()
