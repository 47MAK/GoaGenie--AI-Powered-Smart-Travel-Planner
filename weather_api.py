import requests

API_KEY = "428f0adfc47af6728be8655f34c6bc03"

def get_weather():

    city = "Goa"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # Check if API returned valid data
        if "main" in data and "weather" in data:

            temperature = data["main"]["temp"]
            weather = data["weather"][0]["description"]

            return f"Current temperature in Goa: {temperature}°C | Weather: {weather}"

        else:
            return f"Weather data unavailable: {data.get('message','API error')}"

    except Exception as e:
        return f"Error fetching weather: {str(e)}"