# Today you would be doing  some projects with API


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

` Validate currency codes.`
  
---







A **Movie Search App** is one of the most popular portfolio projects because it combines APIs, search functionality, image handling, and user interfaces.

### What It Does

Users can:

* Search for a movie by title
* View:

  * Release year
  * Rating
  * Plot summary
  * Genre
  * Cast
  * Poster image

---

### Skills You'll Learn

* API requests (`requests`)
* JSON parsing
* Search functionality
* Error handling
* Working with images and URLs
* GUI or web development

---



### Basic Command-Line Version

Install requests:

```bash
pip install requests
```

Example:

```python
import requests

API_KEY = "YOUR_API_KEY"
movie = input("Enter movie title: ")

url = f"https://www.omdbapi.com/?apikey={API_KEY}&t={movie}"

response = requests.get(url)
data = response.json()

if data["Response"] == "True":
    print("Title:", data["Title"])
    print("Year:", data["Year"])
    print("Rating:", data["imdbRating"])
    print("Plot:", data["Plot"])
else:
    print("Movie not found.")
```
```
Implement what you have just learn with a gui of your choice I'll recommended tkinter as that is th one we use
```
---

