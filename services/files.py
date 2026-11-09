import pandas as pd
import os
# Import był nam potrzebny tylko do instalacji
# import openpyxl

# Z danych, które dotarły do mnie w parametrze dataset
# utwórz obiekt DataFrame (pochodzący z Pandas)
def save_to_excel(dataset):
    try:
        # Nowe dane wrzucamy do df
        new_df = pd.DataFrame(dataset)
        # Sprawdź czy ścieżka istnieje
        if os.path.exists('weather.xlsx'):
            # Stare dane odczytujemy - read_ tworzy df
            old_df = pd.read_excel("weather.xlsx")
            # Finalny df składający się z nowych i starych elementów
            df = pd.concat([old_df, new_df])
        else:
            df = new_df

        # DF w zależności którą ścieżką podążył program będzie tylko nowym
        # albo nowym i starym
        df.to_excel("weather.xlsx", index = False)

        print("Dane zostały zapisane w pliku")

    except Exception as e:
        print(e)

def read_excel(file_path: str) -> pd.DataFrame:

    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
                print(f"Wystąpił błąd podczas odczytu pliku: {e}")
                return pd.DataFrame()