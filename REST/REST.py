from fastapi import FastAPI, Depends
from dotenv import load_dotenv, set_key
from pathlib import Path
import os
from Forecast import Forecast
from REST import BaseModels, Current


app = FastAPI()

@app.get("/")
def root():
    return {"status": "OK"}

@app.get("/forecast")
def forecast(city: BaseModels.City = Depends(Current.get_current_city)):

    forecast_data = Forecast.get_forecast(city.city)
    return {"status": "OK", "status_code": 200, "default_city": city.city or "Unset" , "payload": forecast_data}

# curl -X POST -H "Content-Type: application/json" -d "{\"city\": \"London\"}" "http://127.0.0.1:8000/forecast"
@app.post("/forecast")
def change_city(set_city: BaseModels.City):
    CITY = set_city.city

    env_path = Path('.env')
    set_key(env_path, 'CITY', CITY)

    return {"status": "OK", "status_code": 200, "payload": {"city": CITY}}

