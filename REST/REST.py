from fastapi import FastAPI, Depends
from dotenv import set_key
from pathlib import Path
from Forecast import Forecast
from REST import BaseModels, Current


app = FastAPI()

@app.get("/")
def root():
    return {"status": "OK", "status_code": 200}

@app.get("/forecast")
def forecast(city: BaseModels.City = Depends(Current.get_current_city)):

    forecast_data = Forecast.get_forecast(city.city)
    print(f"Forecast call made for {city.city}. Results: {forecast_data}")

    return {"status": "OK" if forecast_data else "ERROR", "status_code": 200 if forecast_data else 404, "default_city": city.city or "Unset" , "payload": forecast_data or {} }


@app.post("/forecast") # curl -X POST -H "Content-Type: application/json" -d "{\"city\": \"London\"}" "http://127.0.0.1:8000/forecast"
def change_city(set_city: BaseModels.City):

    CITY = set_city.city
    set_key(Path('.env'), 'CITY', CITY)

    return {"status": "OK", "status_code": 200, "payload": {"city": CITY}}

