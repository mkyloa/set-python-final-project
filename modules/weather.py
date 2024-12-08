import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(weather_data):
    if weather_data.get('cod') != 200:
        print(f"Error: {weather_data['message']}")
        return

    city = weather_data['name']
    country = weather_data['sys']['country']
    temp = weather_data['main']['temp']
    weather = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print(f"Weather in {city}, {country}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

def main():
    api_key = "03ac1febc8aa27f2df8173046ce3a38a" 
    print("Weather App")
    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()