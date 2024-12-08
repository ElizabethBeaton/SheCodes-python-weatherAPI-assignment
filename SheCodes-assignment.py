import requests
from rich import print
from datetime import datetime

def display_current_weather(city):
    #displays the current weather
    api_key = "1cd294b82d977t5ed35ae2o840f95fe2"
    api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

    response = requests.get(api_url)
    current_weather_data = response.json()
    #print(current_weather_data)
    current_weather_city = current_weather_data['city']
    current_weather_temperature = current_weather_data['temperature']['current']

    #print(f"The temperature in {current_weather_city} today is [green bold]{round(current_weather_temperature)}ºC [/green bold]")
    print(f"Today: [green bold]{round(current_weather_temperature)}ºC [/green bold]")

def display_forecast_weather(city_name):
    api_key = "1cd294b82d977t5ed35ae2o840f95fe2"
    api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city_name}&key={api_key}"

    response = requests.get(api_url)
    forecast_weather_data = response.json()
    print('[red bold]Forecast:[/red bold]')
    #print(forecast_weather_data)
    for day in forecast_weather_data['daily']:
        timestamp = day['time']
        date = datetime.fromtimestamp(timestamp)
        formatted_day = date.strftime("%A")
        # print(formatted_day)
        temperature = day['temperature']['day']

        if date.date() != datetime.today().date():
            print(f"[blue bold]{formatted_day}[/blue bold]: {round(temperature)}ºC  ")

def welcome():
    print("[purple bold]Welcome to my weather app[/purple bold]")

def credit():
    print("\n[yellow]This app was built by Lizzie Beaton")

welcome()
city_name = input("Enter a city ")
city_name = city_name.strip()

if city_name:
    display_current_weather(city_name)
    #print("[green bold]Forecast:[/green bold]")
    display_forecast_weather(city_name)
    credit()
else:
    print("Please try again with a new city")



