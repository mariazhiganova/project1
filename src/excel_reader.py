import pandas as pd


def get_excel(excel_path: str) -> list:
    """
    Функция, для считывания финансовых операций из EXCEL принимает путь к файлу EXCEL в качестве аргумента
    и возвращает список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(excel_path)

        if isinstance(df, pd.DataFrame) and not df.empty:
            return df.to_dict(orient="records")

        return []

    except FileNotFoundError:
        return []
