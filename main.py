import os
import requests
from twilio.rest import Client

OWNM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


paramater = {
    "lat":-28.737810,
    "lon":24.117662,
    "appid": api_key,
    "cnt":4
}

response = requests.get(OWNM_Endpoint, params=paramater)
response.raise_for_status()
data = response.json()
id_weather = data["list"][0]['weather'][0]["id"]

will_rain = False

for hour in data["list"]:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=f"whatsapp:{os.environ.get("Vitual_No")}",
        body="It's going to rain today. Remember to bring an umbrella",
        to=f"whatsapp:{os.environ.get("OWN_No")}"
    )

    print(message.status)
