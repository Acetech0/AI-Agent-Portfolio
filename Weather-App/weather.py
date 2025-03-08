# Weather App using OpenWeatherMap API

import requests

def get_weather(city, api_key):
    """Fetch weather data for a given city."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Extract weather info
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]

            # Display the weather
            print(f"\nWeather in {city}:")
            print(f"Condition: {weather}")
            print(f"Temperature: {temp}°C")
            print(f"Feels Like: {feels_like}°C")
            print(f"Humidity: {humidity}%")
        else:
            print(f"Error: {data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

def main():
    # Replace with your OpenWeatherMap API key
    API_KEY = "8fc3b6716378f2a8e41f74e03828d656"  # Replace this with your API key

    print("Weather App")
    while True:
        city = input("Enter a city name (or 'exit' to quit): ")
        if city.lower() == "exit":
            print("Goodbye!")
            break
        get_weather(city, API_KEY)

if __name__ == "__main__":
    main()