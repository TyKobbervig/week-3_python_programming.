import json

# Simulated API response
response = '''
{
    "city": "Platteville",
    "temperature": 72,
    "condition": "Sunny",
    "humidity": 45
}
'''

# Convert JSON to a Python dictionary
weather_data = json.loads(response)

# Validate required fields
if "city" in weather_data and "temperature" in weather_data:
    print("Weather Report")
    print("--------------")
    print("City:", weather_data["city"])
    print("Temperature:", weather_data["temperature"], "°F")
    print("Condition:", weather_data["condition"])
    print("Humidity:", weather_data["humidity"], "%")
else:
    print("Missing weather data.")