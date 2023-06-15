import requests
from tkinter import *

window = Tk()
window.title("Weather Situation")
window.minsize(width=300, height=300)

label_1 = Label(text="Enter city:")
label_1.pack()
entry_weight = Entry(width=10)
entry_weight.pack(pady=10)

api_key = "https://openweathermap.org/"
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={Enter your API key here}&units=metric'
response = requests.get(url)
data = response.json()

def button_clicked():
    if response.status_code == 200:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        humid = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        print(f'Temperature: {temp} °C')
        print(f'Description: {desc}')
        print(f'Humidity: {humid}')
        print(f'Pressure: {pressure} Pa')
        print(f'Wind: {wind} km/sa')
    else:
        print('Error fetching weather data')

button = Button(text="Calculate", command=button_clicked)
button.pack()

window.mainloop()