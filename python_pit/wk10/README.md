## Python Workshop: Fetching Weather Data via APIs

**Audience:** 13-year-old students with basic Python knowledge (variables, functions, loops)

**Duration:** 60–75 minutes

---

### 1. Objectives

- Understand what an API is and why developers use them
- Learn how to send HTTP requests in Python
- Parse JSON responses
- Build a simple command-line weather app using OpenWeatherMap

### 2. Prerequisites & Setup

1. Python 3 installed on your machine
2. `pip` package manager available
3. Install the `requests` library:
   ```bash
   pip install requests
   ```
4. Your OpenWeatherMap API key (e.g., `930bfccfb3f0cd04fb6f23fa7803e63c`)

---

### 3. Introduction to APIs (10 min)

- **API** stands for _Application Programming Interface_.
- It lets programs talk to each other.
- Real-world analogy: ordering food at a restaurant (you place an order, the kitchen returns your meal).

**Key terms:**
- **Endpoint**: URL where you send requests
- **Request**: Asking for data (`GET`, `POST`)
- **Response**: Data returned, often in JSON format

---

### 4. Testing the Endpoint Directly (5 min)

- **Endpoint:** `https://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=YOUR_API_KEY`
- Paste this URL into your web browser or run:
  ```bash
  curl "https://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=YOUR_API_KEY"
  ```
- Observe the raw JSON response shown in the browser or terminal.

---

### 5. First Python Request: Hardcoded URL (10 min)

```python
# API call
# https://openweathermap.org/current

import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=930bfccfb3f0cd04fb6f23fa7803e63c"
# Fetch and display raw JSON
response = requests.get(url)
print(response.text)
```

---

### 6. Activity: Build & Modulate the URL (15 min)

```python
import requests

# Your API key
api_key = "930bfccfb3f0cd04fb6f23fa7803e63c"

# Variables for city and base endpoint
city = "London"
base_url = "https://api.openweathermap.org/data/2.5/weather"

# Construct URL programmatically using f-string
url = f"{base_url}?q={city}&units=metric&appid={api_key}"
print("Constructed URL:", url)

# Fetch and display raw JSON
response = requests.get(url)
print(response.text)
```

---

### 7. Exploring the JSON (15 min)

Example JSON excerpt:
```json
{
  "weather": [{"description": "light rain", ...}],
  "main": {"temp": 15.0, "pressure": 1012, "humidity": 82},
  "name": "London"
}
```

#### What is JSON?
- JSON stands for **JavaScript Object Notation**.
- It's a way to format data that looks like Python dictionaries: `{ key: value }`.
- When we fetch data from an API, it usually comes as JSON text.

#### Using the `json` Module

```python
#ADD module to your existing code
import json
```

**DELETE** ``` print(response.text) ``` and incorporate this  **snippet** into your existing code

```python
# Turn the text into a Python dictionary
data = json.loads(response.text)

# Now you can access parts of it easily
print("City name:", data['name'])
print("Temperature (°C):", data['main']['temp'])
print("Weather description:", data['weather'][0]['description'])
```

**Important:**
- `json.loads()` = load a JSON string into a Python dictionary.
- Now you can access it just like normal Python data.

#### Quick Exercise:
- Try printing the humidity and pressure from the `main` dictionary!

---

### 8. Exercises (20 min)

**Exercise A:** Change the `city` variable to your hometown and fetch its weather.

**Exercise B:** Ask for two cities in a row and print both temperatures.

**Exercise C (Challenge):**
- Read a list of cities from a Python list
- Loop over each, fetch its temperature in °C
- Store results in a dictionary and print it

---

### 9. Bonus: Error Handling & User Input (20 min)

#### Why Error Handling?
- Sometimes users type the wrong city name.
- Sometimes the internet connection fails.
- Good programs need to handle these problems without crashing!

#### How It Works
- `try` to run some code.
- If an error happens, `except` catches it and lets you respond.

---

#### Step-by-Step: Building Excepts

**Start with a Basic Try-Except**

```python
#Reference to excepts
#https://www.w3schools.com/python/python_try_except.asp
def risky_code():
    print(risky)
    
try:
     risky_code()
except:
     print("Oops! Something went wrong!")

```

- This catches *all* errors.
- Good for beginners, but not specific. It could hide real problems!

**Improve with Specific Exceptions**

Catch only known errors:

```python
#Reference to excepts
#https://www.w3schools.com/python/python_try_except.asp
def risky_code():
    
    print(risky)
    print(0/0)
# try:
#     risky_code()
# except NameError:
#     print("Oops! You entered something wrong!")
# except ZeroDivisionError:
#     print("Oops! You can't divide by zero!")

risky_code()
```

- Now the program knows exactly what error it is dealing with.

#### Apply to our Weather Example

```python
import requests

# Your API key
api_key = "930bfccfb3f0cd04fb6f23fa7803e63c"

city = input("Enter a city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for bad status codes (like 404)
    data = response.json()
    
    # extract and print
    weather_description = data['weather'][0]['description']
    temp_c = data['main']['temp']
    print(f"Weather in {city}: {weather_description}, {temp_c}°C")

except requests.exceptions.HTTPError:
    print("Invalid city name or server error. Please check your spelling!")

except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
```

**Key Concepts:**
- **`raise_for_status()`** checks if the website gave an error.
- **`HTTPError`** handles wrong city names (e.g., typo).
- **`RequestException`** handles internet connection problems.

#### Mini-Challenge
- Try typing a city name wrong (like `Londoon`) to see the error handling in action!
- Try turning off Wi-Fi and seeing the network error catch!

#### Where to Learn More About Exceptions
- **Basic Python Exceptions:** [Python Exceptions Reference (W3Schools)](https://www.w3schools.com/python/python_ref_exceptions.asp)
- **Requests Library Exceptions:** [Requests Exception Handling (Official Requests Docs)](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions)

---

### 10.Visualization using turtle
```python
import requests
import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Weather Visualizer")

# User input
city = screen.textinput("Weather App", "Enter a city:")

# API request
api_key = "930bfccfb3f0cd04fb6f23fa7803e63c"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

response = requests.get(url)
weather_data = response.json()

weather = weather_data['weather'][0]['main'].lower()
temp = weather_data['main']['temp']
humidity = weather_data['main']['humidity']

# Create a turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# Choose color based on weather
if 'rain' in weather:
    color = 'blue'
elif 'cloud' in weather:
    color = 'grey'
elif 'sun' in weather or 'clear' in weather:
    color = 'yellow'
else:
    color = 'green'  # unknown weather fallback

# Draw weather circle
pen.goto(0, 0)
pen.fillcolor(color)
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Write temperature and humidity
pen.goto(-70, -80)
pen.write(f"Temp: {temp} °C", font=("Arial", 14, "bold"))
pen.goto(-70, -110)
pen.write(f"Humidity: {humidity}%", font=("Arial", 14, "bold"))

screen.mainloop()
```



- **Plotting:** Use `matplotlib` to chart temperatures of multiple cities.
- **GUI:** Build a simple window with `tkinter`.
- **Web App:** Flask or Streamlit for a web interface.

---

**Questions?** Let's run through any code together!
