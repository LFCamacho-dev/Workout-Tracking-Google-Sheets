import os
import requests
import datetime as dt

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_KEY = os.environ.get("SHEETY_AUTH")
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

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

nutri_response = requests.post(url=NUTRI_ENDPOINT, json=n_params, headers=headers)
nutri_response.raise_for_status()
nutri_data = nutri_response.json()
print(nutri_data)

workouts = nutri_data['exercises']

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%H:%M:%S")
# now_time = dt.datetime.now().strftime("%X")

SHEETY_ENDPOINT = "https://api.sheety.co/bf637b0f90dd7856fb44c4190b0e1659/workoutTracking/workouts"

sheety_headers = {
    "Authorization": SHEETY_KEY,
    "content-type": "application/json",
}

for exercise in workouts:
    sheety_params = {
        "workout": {
            "date": f"{today_date}",
            "time": f"{now_time}",
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_post_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_headers)
    print(sheety_post_response.text)

    sheety_response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
    sheety_response.raise_for_status()
    sheety_data = sheety_response.text
    print(sheety_data)
