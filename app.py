# For individuals using the weather API:
# - Using the Forecast API, request the weather forecast for the next 3 days for your local zip code
# - Extract daily forecast information into a csv file named “daily_forecast.csv” with the following fields:
# 	- zipcode
# 	- date
# 	- maxtemp_f
# 	- mintemp_f
# 	- avgtemp_f
# 	- daily_chance_of_rain
# 	- daily_chance_of_snow
# 	- condition.text
# 	- condition.icon
# - Extract hourly forecast information into a csv file named “hourly_forecast.csv” with the following fields:
# - zipcode
# 	- date
# 	- time
# 	- temp_f
# 	- feelslike_f
# 	- heatindex_f
# 	- windchill_f
# 	- humidity
# 	- cloud
# 	- chance_of_rain
# 	- chance_of_snow
# 	- condition.text
# 	- condition.icon

import requests
import json
import pandas as pd
import os
from fastapi import FastAPI, Form

# load api key from config or env var
api_key = os.getenv('WEATHER_API_KEY')
if not api_key:
    with open("config.json") as f:
        data = json.load(f)
        api_key = data["api_key"]

url = "https://api.weatherapi.com/v1/forecast.json"

params = {
    "key": api_key,
    "q": "72734",
    "days": "3",
    "aqi": "no",
    "alerts": "no",
}

req = requests.get(url, params=params)
# df = pd.read_json(req.content)
# print(df.head())
app = FastAPI()

@app.get("/")
async def index():
    return {"req.content": req.content}