import numpy
import requests
import json

api_key = "de63b9c282b2bfb002b74dff9e8b9fc5"
city_name = input("Enter city name: ")

lat = "http://api.openweathermap.org/geo/1.0/direct?q=" + city_name + "&limit=5&appid=" + api_key
responseLat = requests.get(lat)

x = responseLat.json()

print("Response from Geo API: ", x)

if isinstance(x, list) and len(x) > 0:
    if "lat" in x[0] and "lon" in x[0]:
        base_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(x[0]["lat"]) + "&lon=" + str(x[0]["lon"]) + "&appid=" + api_key
        response = requests.get(base_url)
        x = response.json()

        if x["cod"] != 404:
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature = numpy.round((current_temperature - 273.15) * 9/5 + 32)

            feels_like = y["feels_like"]
            feels_like = numpy.round((feels_like - 273.15) * 9/5 + 32)
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]

            min_temp = y["temp_min"]
            min_temp = numpy.round((min_temp - 273.15) * 9/5 + 32)
            max_temp = y["temp_max"]
            max_temp = numpy.round((max_temp - 273.15) * 9/5 + 32)

            z = x["weather"]
            weather_description = z[0]["description"]

            print(" Temperature (in Fahrenheit unit) = " + str(current_temperature) +
                  "\n Feels like = " + str(feels_like) +
                  "\n Atmospheric pressure (in hPa unit) = " + str(current_pressure) +
                  "\n Humidity (in percentage) = " + str(current_humidity) +
                  "\n Description = " + str(weather_description) +
                  "\n Minimum temperature = " + str(min_temp) +
                  "\n Maximum temperature = " + str(max_temp))
        else:
            print("City weather data not found.")
    else:
        print("Latitude and Longitude not found in response.")
else:
    print("City not found in Geo API.")
