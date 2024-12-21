import pandas as pd


def get_excel(excel_path: str) -> list:
    try:
        df = pd.read_excel(excel_path)

        if isinstance(df, pd.DataFrame) and not df.empty:
            return df.to_dict(orient="records")

        return []

    except FileNotFoundError:
        return []

    except Exception:
        return []


if __name__ == "__main__":
    print(get_excel("..\\data\\transactions.xlsx"))
