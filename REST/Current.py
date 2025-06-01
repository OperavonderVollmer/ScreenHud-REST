from dotenv import load_dotenv
from REST import BaseModels
import os
from pathlib import Path


def get_current_city() -> BaseModels.CityIdentifier:
    load_dotenv(dotenv_path=Path('.env'), override=True)    
    city = BaseModels.CityIdentifier(city=str(os.getenv("CITY", "")))
    print(f"Current city: {city.city}")
    return city


# pip install --upgrade git+https://github.com/OperavonderVollmer/ScreenHUD-Alarm