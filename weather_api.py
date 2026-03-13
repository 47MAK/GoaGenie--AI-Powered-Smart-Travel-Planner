import requests

API_KEY = "428f0adfc47af6728be8655f34c6bc03"

def get_weather():

    city = "Goa"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        return f"{temp}°C, {desc}"

    except:
        return "Weather data unavailable"