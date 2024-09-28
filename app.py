from flask import Flask, render_template, request
import requests
import creds  # Ensure creds.py has your API key

app = Flask(__name__)

# Function to get weather info from OpenWeatherMap API
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={creds.API_key}"
    res = requests.get(url)
  
    if res.status_code == 404:
        return None
    
    # Parse the response JSON to get weather info
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    # Get the icon URL and return all the weather info
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle weather search
@app.route('/get_weather', methods=['POST'])
def get_weather_route():
    city = request.form['city']  # Retrieve city from the form input
    result = get_weather(city)
    
    if result is None:
        return render_template('index.html', error="City not found!")
    
    icon_url, temperature, description, city, country = result
    return render_template('result.html', icon_url=icon_url, temperature=temperature, 
                           description=description, city=city, country=country)

if __name__ == '__main__':
    app.run(debug=True)