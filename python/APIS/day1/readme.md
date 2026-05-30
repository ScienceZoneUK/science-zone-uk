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






A **Currency Converter** is an excellent beginner-to-intermediate Python project because it's simple to build but introduces APIs, user input, error handling, and data processing.

### Features

#### Basic Version

* Enter an amount
* Select source currency (USD, GBP, EUR, etc.)
* Select target currency
* Display converted amount

#### Intermediate Version

* Support 100+ currencies
* Show exchange rates
* Conversion history
* Save favorite currencies
* Command-line menu system

#### Advanced Version

* GUI with Tkinter
* Historical exchange rates
* Exchange-rate charts
* Real-time auto-refresh
* Web app using Flask

---

### Project Structure

```text
currency-converter/
│
├── main.py
├── converter.py
├── config.py
└── requirements.txt
```

---

### Install Dependency

```bash
pip install requests
```

---

### Example Using ExchangeRate API

```python
import requests

amount = float(input("Amount: "))
from_currency = input("From (USD, GBP, EUR): ").upper()
to_currency = input("To: ").upper()

url = f"https://open.er-api.com/v6/latest/{from_currency}"

response = requests.get(url)
data = response.json()

if to_currency in data["rates"]:
    rate = data["rates"][to_currency]
    converted = amount * rate

    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
else:
    print("Invalid currency code")
```

---

### Challenges to Add

1. Validate currency codes.
2. Handle internet connection errors.
3. Show top 10 exchange rates.
4. Store conversion history in SQLite.
5. Build a graphical interface using Tkinter.
6. Add a currency search feature.
7. Export conversion history to CSV.

---

### Skills You'll Learn

* REST APIs
* JSON data handling
* Python functions
* Exception handling
* File/database storage
* GUI development
* Working with real-time data

---

### Portfolio Upgrade

Create a **Finance Dashboard** that combines:

* Currency Converter
* Cryptocurrency Tracker
* Stock Prices
* Expense Tracker

This turns a simple converter into a project that demonstrates API integration, data visualization, and full-stack development skills.


