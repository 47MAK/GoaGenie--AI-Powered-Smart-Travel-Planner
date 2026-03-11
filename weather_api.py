import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"

def get_weather():

    city = "Goa"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    return f"Current temperature in Goa: {temperature}°C, Weather: {weather}"