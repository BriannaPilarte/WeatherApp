# Weather API Script (Edited)
# by Brianna Pilarte
# Project Starting point provided by https://www.youtube.com/watch?v=9P5MY_2i7K8&ab_channel=NeuralNine
#[GitHub - BriannaPilarte/WeatherApp](https://github.com/BriannaPilarte/WeatherApp)


import datetime as dt
import requests

def k_c_f(k):
    c = k - 273.15
    f = c * (9/5) + 32
    return c, f

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    url = f"{base_url}?appid={api_key}&q={city}"
    
    try:
        response = requests.get(url).json()
        return response
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    api_key = open('locked.txt', 'r').read()

    city = input("Enter the city: ")

    response = get_weather(api_key, city)
    
    if response:
        temp_k = response['main']['temp']
        temp_c, temp_f = k_c_f(temp_k)
        feels_like_k = response['main']['feels_like']
        feels_like_c, feels_like_f  = k_c_f(feels_like_k)
        wind_speed = response['wind']['speed']
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
        sunrise = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

        print(f"Temperature in {city} is currently {temp_c:.2f}C or {temp_f:.2f}F.")
        print(f"It feels like {feels_like_c:.2f}C or {feels_like_f:.2f}F in {city} today.")
        print(f"The wind speed in {city} is {wind_speed}m/s.")
        print(f"Humidity in {city} is currently {humidity}%.")
        print(f"{description} in {city}.")
        print(f"Sunrise is at {sunrise} in {city}.")
        print(f"Sunset is at {sunset} in {city}.")

if __name__ == "__main__":
    main()
