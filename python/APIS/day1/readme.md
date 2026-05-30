A **Weather App** is one of the best intermediate Python projects because it teaches APIs, JSON, error handling, and user interfaces.

### Features


* Enter a city name
* Fetch current weather
* Display:

  * Temperature
  * Weather condition
  * Humidity
  * Wind speed


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

