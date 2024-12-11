import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(numbers: str) -> str:
    """
    Функция, возвращающая замаскированный номер карты
    """
    logger.info("Выполняется проверка на корректность номера карты")

    if len(numbers) != 16 or not numbers.isdigit():
        logger.error("Номер карты не соответствует заданному формату")
        raise ValueError("Неверный номер карты")

    logger.info("Номер карты успешно замаскирован")
    return numbers[:4] + " " + numbers[4:6] + "** ****" + " " + numbers[-4:]


def get_mask_account(numbers: str) -> str:
    """
    Функция, возвращающая замаскированный номер счета в формате ** и четырех последних цифр
    """
    logger.info("Выполняется проверка на корректность номера счёта")

    if len(numbers) != 20 or not numbers.isdigit():
        logger.error("Номер счёта не соответствует заданному формату")
        raise ValueError("Неверный номер счёта")

    logger.info("Номер счёта успешно замаскирован")
    return f"**{numbers[-4:]}"
