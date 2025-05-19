from dotenv import load_dotenv
from REST import BaseModels
import os
from pathlib import Path


def get_current_city() -> BaseModels.City:
    load_dotenv(dotenv_path=Path('.env'), override=True)    
    city = BaseModels.City(city=str(os.getenv("CITY", "")))
    print(f"Current city: {city.city}")
    return city
