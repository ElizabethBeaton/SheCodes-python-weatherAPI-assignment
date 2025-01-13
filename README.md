# SheCodes-PythonBasics-FinalAssignment

## Python Weather App Forecast

* Welcome to the Weather App! This project allows users to check the current weather and a 7-day forecast for any city worldwide. The app leverages the SheCodes Weather API to fetch real-time weather data and displays it using the Python rich library for colorful terminal output.

###Features

* **Current Weather**: Displays the current temperature for a given city.
* **7-Day Forecast**: Provides a daily forecast with temperatures for the next seven days.
* **User-Friendly Interface**: Includes a welcome message and colored output for better readability.

---

### Installation

1. Clone the repository:

git clone https://github.com/yourusername/weather-app.git
cd weather-app

2. Install the required dependencies:

pip install requests rich

3. Run the script:

python weather_app.py

---

### Usage
1. Launch the script by running:
   
python weather_app.py

3. Enter the name of a city when prompted. For example:

Enter a city: Paris

3. The current temperature and the 7-day weather forecast will be displayed.

---

### API Integration

This application uses the SheCodes Weather API to fetch weather data. You need an API key to access this service, which is embedded in the script for demonstration purposes.

#### API Endpoints:

1. **Current Weather**:

* URL: https://api.shecodes.io/weather/v1/current
* Method: GET
* Query Parameters:
- query (string): Name of the city (e.g., Paris).
- key (string): API key (e.g., 1cd294b82d977t5ed35ae2o840f95fe2).

2. **7-Day Forecast**:

* URL: https://api.shecodes.io/weather/v1/forecast
* Method: GET
* Query Parameters:
- query (string): Name of the city (e.g., London).
- key (string): API key.

### Data Structure

#### Current Weather Response:

The API returns a JSON object with the following structure:

{
  "city": "London",
  "temperature": {
    "current": 8.5
  }
}

* city (string): Name of the city.
* temperature.current (float): Current temperature in Celsius.

### 7-Day Forecast Response:

The API returns a JSON object with the following structure:

{
  "daily": [
    {
      "time": 1672527600,
      "temperature": {
        "day": 10.5
      }
    },
    ...
  ]
}

* daily (array): List of daily forecasts.

- time (int): Unix timestamp for the forecast day.

- temperature.day (float): Forecasted temperature for the day in Celsius.

#### Example Output

Welcome to my weather app

Enter a city: Paris
Today: 12ºC

Forecast:
Monday: 14ºC
Tuesday: 15ºC
Wednesday: 16ºC
Thursday: 14ºC
Friday: 12ºC
Saturday: 10ºC
Sunday: 9ºC

This app was built by Lizzie Beaton

