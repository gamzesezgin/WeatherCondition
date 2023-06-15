import requests
import json

def get_weather(api_key, city):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q":city, "appid":api_key, "units": "metric"}

    response = requests.get(url, params=params)
    data = response.json()

    if data["cod"] == 200:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        humid = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        print(f'Temperature: {temp} °C')
        print(f'Description: {desc}')
        print(f'Humidity: {humid}%')
        print(f'Pressure: {pressure} Pa')
        print(f'Wind: {wind} km/sa')
    else:
        print('Error fetching weather data')

api_key = "https://openweathermap.org/"
city = input("Enter city: ")

get_weather(api_key, city)
