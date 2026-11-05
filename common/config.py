from dotenv import load_dotenv
import os

load_dotenv()

class AppConfig:
    # serwerze - wartość dla zmiennej API_KEY weź z pliku .env ze zmiennej API_KEY
    API_KEY = os.getenv("API_KEY")
    CITY = "Lisbon"
    FILENAME = "weather.xlsx"
