# To install: pip install requests
# Requires a free API key from a service like OpenWeatherMap

import requests
import json

# IMPORTANT: Replace "YOUR_API_KEY_HERE" with your actual, personal API key.
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city_name):
    """Fetches and displays current weather for a specified city."""
    url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        description = weather['description']
        humidity = main['humidity']
        
        print(f"\nWeather in {city_name.title()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.title()}")
        print(f"Humidity: {humidity}%")
    else:
        print("Error: Could not retrieve weather data. Check the city name or API key.")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)