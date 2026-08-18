# Tkinter Weather App

A Python desktop weather application that evolved from my earlier command-line `WeatherApp-project`.

This version moved beyond hard-coded weather data by connecting to the OpenWeatherMap API and introduced a graphical interface using Tkinter and ttkbootstrap. It displays live weather information for a searched city, including temperature, conditions and a weather icon.

## What Changed From the Earlier Version

- Replaced the terminal interface with a desktop GUI
- Replaced hard-coded sample data with live API data
- Added city search and basic error handling
- Added weather icons and a styled interface

## Retrospective Context

Building this version helped me understand both the advantages and limitations of a desktop GUI. I later explored moving the weather-app concept toward a web application so that it could be accessed through a browser rather than requiring a local Tkinter environment.

This repository is kept as part of my development history and shows the progression of the project rather than representing its final possible form.

## Built With

- Python
- Tkinter / ttkbootstrap
- OpenWeatherMap API
- Requests
- Pillow

## API Key

The application expects OpenWeatherMap credentials locally. API keys or other secrets should not be committed to the repository.
