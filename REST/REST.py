from fastapi import FastAPI, Depends
from dotenv import set_key
from pathlib import Path
from Forecast import Forecast
from REST import BaseModels, Current, AlarmConnection
from Alarm import Alarm



app = FastAPI()

@app.get("/")
def root():
    return {"status": "OK", "status_code": 200}

@app.get("/forecast")
def forecast(city: BaseModels.CityIdentifier = Depends(Current.get_current_city)):

    forecast_data = Forecast.get_forecast(city.city)
    print(f"Forecast call made for {city.city}. Results: {forecast_data}")

    return {"status": "OK" if forecast_data else "ERROR", "status_code": 200 if forecast_data else 404, "default_city": city.city or "Unset" , "payload": forecast_data or {} }


@app.post("/forecast") # curl -X POST -H "Content-Type: application/json" -d "{\"city\": \"London\"}" "http://127.0.0.1:8000/forecast"
def change_city(set_city: BaseModels.CityIdentifier):

    CITY = set_city.city
    set_key(Path('.env'), 'CITY', CITY)

    return {"status": "OK", "status_code": 200, "payload": {"city": CITY}}

@app.post("/alarms/new")
def new_alarm(alarm: Alarm.Alarm):
    resp = AlarmConnection.add_alarm(alarm)
    return {"status": "OK", "status_code": 200, "payload": {"response": resp}}

@app.get("/alarms/list")
def list_alarms():
    resp = AlarmConnection.list_alarms()
    return {"status": "OK", "status_code": 200, "payload": {"response": resp}}

@app.get("/alarms/start_all")
def start_all_alarms():
    resp = AlarmConnection.start_all_alarms()
    return {"status": "OK", "status_code": 200, "payload": {"response": resp}}

@app.post("/alarms/start")
def start_alarm(alarm: BaseModels.AlarmIdentifier):
    resp = AlarmConnection.start_alarm(alarm.title)
    return {"status": "OK", "status_code": 200, "payload": {"response": resp}}

@app.post("/alarms/clear")
def clear_alarm(alarm: BaseModels.AlarmIdentifier):
    resp = AlarmConnection.start_alarm(alarm.title)
    return {"status": "OK", "status_code": 200, "payload": {"response": resp}}

@app.post("/alarms/clear_all")
def clear_all_alarms():
    resp = AlarmConnection.clear_all_alarms()
    return {"status": "OK", "status_code": 200, "payload": {"response": resp}}

@app.post("/alarms/set_auto_start")
def set_auto_start(t: str):
    resp = AlarmConnection.set_auto_start(t)
    return {"status": "OK", "status_code": 200, "payload": {"response": resp}}

@app.post("/alarms/set_auto_save")
def set_auto_save(t: str):
    resp = AlarmConnection.set_auto_save(t)
    return {"status": "OK", "status_code": 200, "payload": {"response": resp}}