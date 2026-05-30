A **Weather App** is one of the best intermediate Python projects because it teaches APIs, JSON, error handling, and user interfaces.

### Features

**Basic Version**

* Enter a city name
* Fetch current weather
* Display:

  * Temperature
  * Weather condition
  * Humidity
  * Wind speed

**Advanced Version**

* 5-day forecast
* Weather icons
* Search history
* GPS/location support
* Graphs and charts
* Desktop GUI or web interface

---

### Technologies

| Part               | Tool                         |
| ------------------ | ---------------------------- |
| Language           | Python                       |
| API                | OpenWeatherMap or WeatherAPI |
| HTTP Requests      | `requests`                   |
| GUI (optional)     | `tkinter`                    |
| Web App (optional) | Flask                        |
| Data Storage       | SQLite or JSON               |

---

### Project Structure

```text
weather-app/
│
├── main.py
├── config.py
├── weather.py
├── requirements.txt
└── assets/
```

---

### Install Dependencies

```bash
pip install requests
```

---

### Example Code

```python
import requests

API_KEY = "YOUR_API_KEY"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
else:
    print("City not found")
```

---

### Skills You'll Learn

* Working with REST APIs
* Sending HTTP requests
* Parsing JSON data
* Functions and modules
* Error handling
* GUI development (if using Tkinter)
* Web development (if using Flask)

---

### Resume Upgrade Ideas

1. Add a 7-day forecast.
2. Create a modern GUI using Tkinter.
3. Build a web version with Flask.
4. Add weather charts using Matplotlib.
5. Deploy online using [Render](https://render.com?utm_source=chatgpt.com) or [PythonAnywhere](https://www.pythonanywhere.com?utm_source=chatgpt.com).

A Flask-based weather dashboard with search, forecasts, and charts is a strong portfolio project for internships and entry-level Python roles.
