import requests

# OpenWeatherMap API credentials
API_KEY = "Your API Key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

while True:
    # Ask the user for a city
    city = input("\n🏙️ Enter city name (or type 'exit' to quit): ").strip()

    if city.lower() == "exit":
        print("👋 Exiting Weather App. Goodbye!")
        break

    # Prepare request parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    # Send request to OpenWeatherMap API
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Parse and display the weather data
    if data.get("cod") == 200:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌤️ Weather in {city.title()}:")
        print(f"🌡️ Temperature : {temperature} ℃")
        print(f"📋 Description : {description}")
        print(f"💧 Humidity    : {humidity}%")
        print(f"🌬️ Wind Speed  : {wind_speed} m/s")
    else:
        print("❌ City not found. Please check the name and try again.")
