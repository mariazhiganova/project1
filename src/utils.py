import json
import logging
from typing import Optional

from settings import LOG_UTILS_PATH


def get_transaction_data(json_file: Optional[str] = None) -> list:
    """
    Функция, которая принимает путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    """
    logger = logging.getLogger("utils")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(LOG_UTILS_PATH, mode="w", encoding="utf-8")
    file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    try:
        logger.info("Попытка открыть json-файл.")

        if json_file is not None:
            logger.info("Json-файл успешно открывается для чтения.")

            with open(json_file, "r", encoding="utf-8") as f:
                logger.info("Загрузка данных из json-файла и преобразование в Python-объект.")

                transactions_list = json.load(f)
                logger.info("Проверка: является ли содержимое файла списком.")

                if isinstance(transactions_list, list):
                    logger.info("Содержимое файла является списком.")
                    logger.info("Данные в формате Python-объекта получены успешно.")

                    return transactions_list

        logger.error("Файл отсутствует")
        return []

    except FileNotFoundError:
        logger.error(f"Файл по пути {json_file} не найден.")
        return []

    except json.JSONDecodeError as ex:
        logger.error("Данные из json-файла не соответствует синтаксису JSON или содержат ошибочные данные")
        logger.error(f"Ошибка {ex}")

        return []
