import requests
import config

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to get weather data for a city
def get_weather_data(city, units="metric"):
    try:
        # Make sure to URL-encode the city name
        city = requests.utils.quote(city)

        # Create the API request URL
        request_url = f"{BASE_URL}?appid={config.API_KEY}&q={city}&units={units}"

        # Send a GET request to the API
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()
            weather_description = data['weather'][0]['description']
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            return {
                "city": city,
                "weather_description": weather_description,
                "temperature": temperature,
                "humidity": humidity,
                "wind_speed": wind_speed
            }
        else:
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

# Function to display weather information
def display_weather_info(weather_data, units="metric"):
    if weather_data:
        temperature_unit = "°C" if units == "metric" else "°F"
        wind_speed_unit = "m/s" if units == "metric" else "mph"

        print(f"Weather in {weather_data['city']}: {weather_data['weather_description']}")
        print(f"Temperature: {weather_data['temperature']}{temperature_unit}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} {wind_speed_unit}")
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    units = input("Enter preferred units (metric/imperial): ").lower()

    weather_data = get_weather_data(city, units)
    display_weather_info(weather_data, units)