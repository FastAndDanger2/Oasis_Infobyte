import tkinter as tk
from tkinter import ttk, messagebox
import requests
import numpy

api_key = "de63b9c282b2bfb002b74dff9e8b9fc5"

def get_weather():
    city_name = city_entry.get()
    if not city_name:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return
    
    lat_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}"
    try:
        responseLat = requests.get(lat_url)
        x = responseLat.json()

        if isinstance(x, list) and len(x) > 0:
            if "lat" in x[0] and "lon" in x[0]:
                base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={x[0]['lat']}&lon={x[0]['lon']}&appid={api_key}"
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

                    result_label.config(
                        text=f"Temperature: {current_temperature}°F\n"
                             f"Feels Like: {feels_like}°F\n"
                             f"Pressure: {current_pressure} hPa\n"
                             f"Humidity: {current_humidity}%\n"
                             f"Description: {weather_description.capitalize()}\n"
                             f"Min Temp: {min_temp}°F\n"
                             f"Max Temp: {max_temp}°F"
                    )
                else:
                    messagebox.showerror("Error", "City weather data not found.")
            else:
                messagebox.showerror("Error", "Latitude and Longitude not found in response.")
        else:
            messagebox.showerror("Error", "City not found in Geo API.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

app = tk.Tk()
app.title("Weather Info")
app.geometry("400x500")
app.configure(bg="#30475E")

title_label = tk.Label(app, text="Weather Info", font=("Arial", 16, "bold"), bg="#30475E", fg="#F5F5F5")
title_label.pack(pady=(10, 0))

city_label = tk.Label(app, text="Enter City Name", font=("Arial", 12), bg="#30475E", fg="#F5F5F5")
city_label.pack(pady=(10, 5))

city_entry = tk.Entry(app, font=("Arial", 12), width=25)
city_entry.pack(pady=5)

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather, font=("Arial", 12), bg="#F05454", fg="#F5F5F5", activebackground="#D94343", activeforeground="#F5F5F5", bd=0, padx=10, pady=5)
get_weather_button.pack(pady=20)

result_label = tk.Label(app, text="", font=("Arial", 12), bg="#30475E", fg="#F5F5F5", justify="left")
result_label.pack(pady=10)

app.mainloop()
