import os
import requests

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content - Type": "application / json",
}

n_params = {
    "query": "ran 3 miles",
    "gender": "male",
    "weight_kg": 99.5,
    "height_cm": 186.64,
    "age": 40
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=n_params, headers=headers)
response.raise_for_status()
data = response.json()
print(data)


