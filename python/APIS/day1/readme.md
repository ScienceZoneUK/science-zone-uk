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

### APIs You Can Use

* [OMDb API](https://www.omdbapi.com/?utm_source=chatgpt.com) (easy for beginners)
* [TMDB API Documentation](https://developer.themoviedb.org/docs/getting-started?utm_source=chatgpt.com) (more features and better images)

For a portfolio project, TMDB is usually the better choice.

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

---

### Intermediate Features

#### Search Multiple Movies

```python
https://www.omdbapi.com/?apikey=KEY&s=batman
```

Show a list of matching movies instead of only one result.

#### Save Favorites

Store favorite movies in:

* JSON
* CSV
* SQLite

#### Movie Recommendations

Display:

* Similar movies
* Same genre movies
* Top-rated movies

---

### Flask Web App Structure

```text
movie-search-app/
│
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│
└── database.db
```

Features:

* Search bar
* Poster display
* Movie details page
* Favorite movies list

---

### Advanced Features

#### 1. Trending Movies

Use TMDB's trending endpoint.

#### 2. Watchlist

Users can:

* Add movies
* Remove movies
* Mark as watched

#### 3. User Accounts

Build login and registration with:

* Flask
* SQLite

#### 4. Movie Review System

Allow users to:

* Rate movies
* Write reviews

#### 5. Recommendation Engine

Recommend movies based on:

* Genre
* Ratings
* Viewing history

---

### Resume-Worthy Version

Build a **Netflix-style Movie Explorer** with:

* Flask backend
* TMDB API
* SQLite database
* User authentication
* Watchlist
* Search
* Trending movies
* Recommendations

This project demonstrates:

* APIs
* Databases
* Authentication
* Web development
* CRUD operations
* Frontend design

It's a strong project for junior Python, web development, or software engineering portfolios.


This turns a simple converter into a project that demonstrates API integration, data visualization, and full-stack development skills.


