# 1: Create accont on OpenWeatherMap and API key

# 2: Import required modules
import tkinter as tk # For our GUI
import requests # Allows us to make //http requests
from tkinter import messagebox
from PIL import Image, ImageTk # Proccessing and displaying images
import ttkbootstrap
import creds


# Function to get weather info from OpenWeatherMap API
# It returns as a tuple containing icon, url, temperature, weather description, city, and country.
def get_weather(city):
  
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={creds.API_key}"
  res = requests.get(url)
  
  if res.status_code == 404:
    messagebox.showerror("Error, City not found")
    return None
  
  # Parse the response JSON to get weather info
  weather = res.json()
  print(weather)
  icon_id = weather['weather'][0]['icon']
  temperature = weather['main']['temp'] - 273.15
  description = weather['weather'][0]['description']
  city = weather['name']
  country = weather['sys']['country']

  #Get the icon URL and return all the weather info
  icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
  return (icon_url, temperature, description, city, country)

# Function that searches for the weather of desired city
def search():
  city = city_entry.get() # Retrieves user input from the Entry widget
  result = get_weather(city) # Retrieves data from specified location and updates the GUI with the aquired data
  if result is None:
    return
  # If the city is found, unpack the weather info 
  icon_url, temperature, description, city, country = result
  location_label.configure(text=f"{city}, {country}")
  
  # Get the weather icon image from the URL and update the icon label
  image = Image.open(requests.get(icon_url, stream=True).raw)
  icon = ImageTk.PhotoImage(image)
  icon_label.configure(image=icon)
  icon_label.image = icon 
  
  # Update the temperature and the description labels
  temperature_label.configure(text=f"Temperature: {temperature:.2f}˚C")
  description_label.configure(text=f"Description: {description}")

# Create the main program that creates our GUI window
root = ttkbootstrap.Window(themename="morph") 
root.title("Weather App")
root.geometry("400x400")


# Entry widget (where we enter desired location)
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

# Button widget (search for info on the weather)
search_btn = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_btn.pack(pady=10)

# Label widget (location name)
location_label = tk.Label(root)
location_label.pack()

# Icon widget (weather icon)
icon_label = tk.Label(root)
icon_label.pack()

# Label widget (show temperature)
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

# Label widget (to show the weather description)
description_label = tk.Label(root)
description_label.pack()

root.mainloop()