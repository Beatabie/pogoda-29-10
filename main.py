# Ze ścieżki services/openweather importuj element get_weather
from services.openweather import get_weather
from services.files import save_to_excel
import time

while True:
    # Pod zmienną weather kryją się pobrane - aktualne dane pogodowe
    weather = get_weather()
    save_to_excel([weather])
    # Po każdej iteracji śpij na X czasu
    # zapobiegnie to nieskończonej pętli - tysiące razy na sekundę
    time.sleep(15)

# Serwis 1: Pobieranie danych pogodowych

# Serwis 2: Zapis wcześniej pobranych danych do excela


# Serwis 1: Pobieranie danych pogodowych

# Serwis 2: Zapis wcześniej pobranych danych do excela

print(weather)
