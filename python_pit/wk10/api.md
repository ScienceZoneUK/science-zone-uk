# Finding api's

Search for fun apis to test your skills in using them!
[List of api's](https://github.com/public-apis/public-apis)

## Raw endpoints

Are you able to use the api's?

- [Dog facts](https://dogapi.dog/api/v2/facts)    
- [Bank Holidays](https://www.gov.uk/bank-holidays.json)
- [Carbon Intensity API](https://api.carbonintensity.org.uk/intensity)  

------- 
## Exchange rates

Currency conversion is a common operation used by people, banks, exchange bureaus etc.
### Task
- How do you convert currencies, what do you need?
- How would a computer convert a currency?


[Currencies-GBP](https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/gbp.json)    
We can access data online and interface with it through an API or application programs interface. We can communicate with an online    
application, in our case data on currencies, and ask it specific things.


### Requesting data
[w3schools-requests](https://www.w3schools.com/python/module_requests.asp)

Applications running on the internet may allow us to communicate with them and ask for specific info, in our case exchange rates.    
The Python module ```import requests``` simplifies the process for us!    
We then use a url to build a query and request data      
``` https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/gbp.json ```.   
Generally, when we request information, the data will be returned as a file or a webpage.     
We must save our response ``` response = requests.get(url) ```.   


-------

```python
import requests

#Build the URL in sections for legibility
base_url = "https://cdn.jsdelivr.net/npm/@fawazahmed0"
endpoint = "/currency-api@latest/v1/currencies/"
base_curr = "gbp"
data_type = ".json"
url = f"{base_url}{endpoint}{base_curr}{data_type}"

#Request the data
response = requests.get(url)

#Save the response as a JSON into a dictionary
data = response.json()

#Print the data
print(data)

#get the exchange rate
rate = data["gbp"]["eur"]

#Print the exchange rate
print(rate)

```
- What does JSON stand for?
- Step through the code and understand it
- Keep the base as 'gbp' and modify the conversion - 'gbp' to .....?
- If you enter the wrong currency, what's the error?
- Using the browser URL, get all the available currencies ```https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json```
- See program below, run it, step through it 
```python
import requests

#Setup the url
url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json"

#request the data and save it
response = requests.get(url)

#Convert json into a dict using python method
data = response.json()
print(data)
```
Can you use ``` input() ``` to get a base currency and check it exists, put it all in a function?

```python
def my_func():
    user = input('get some user data\n')
    if user in data:
        print("yey")
    else:
        print("Try again")

while True:
    my_func()

```


- Write a try and except to catch the error and print a meaningful message        
  Errors interupt and crash programs, python try:except catch them and keep everything running.       
  reference: [Try:except](https://www.geeksforgeeks.org/python-try-except/)

```python
import requests

url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json"
response = requests.get(url)
data = response.json()

def my_func():
    user = input('\nget some user data\n')
    if user not in data:
        raise ValueError ("You created an error")
    else:
        print("Yes currency available")

while True:
    try:
        my_func()
        
    except ValueError as e:
        print(f"{e}, try again!!")
        
```
- Write some more meaningful messages


------

- Predict what the code below will do
  
```python
import requests

url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json"
response = requests.get(url)
data = response.json()

def get_currency():
    currency = input('Enter a currency code (like usd, eur, gbp):\n').lower()
    if currency not in data:
        raise ValueError("Invalid currency code entered.")
    number = get_value()
    print(f"You chose {currency} and entered the number {number}")
    print(f"Currency name: {data[currency]}")

def get_value():
    value = input('Enter a whole number:\n')
    if not value.isdigit():
        raise ValueError("You didn't enter a whole number.")
    return int(value)

def run():
    try:
        get_currency()
    except ValueError as e:
        print(e)

while True:
    run()

```
- Create a new program and run code
- Now step through code to fully understand it

-------


```python
import turtle
import requests

# Setup turtle screen
screen = turtle.Screen()
screen.title("Simple Currency Converter")
screen.setup(600, 400)
screen.bgcolor("lightblue")

# Create turtle to display text
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Get currency data from API
def get_rate(base, target):
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{base.lower()}.json"
    response = requests.get(url)
    data = response.json()
    rate = data[base.lower()][target.lower()]
    return rate

# Convert and display currency
def convert():
    base_currency = screen.textinput("Currency Converter", "Enter base currency (e.g. EUR, USD, GBP):").upper()
    target_currency = screen.textinput("Currency Converter", "Enter target currency (e.g. EUR, USD, GBP):").upper()
    amount = float(screen.textinput("Currency Converter", f"Enter amount in {base_currency}:"))

    try:
        rate = get_rate(base_currency, target_currency)
        converted_amount = amount * rate
        writer.clear()
        writer.goto(0, 0)
        writer.write(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}", align="center", font=("Arial", 20, "bold"))
    except:
        writer.clear()
        writer.goto(0, 0)
        writer.write("Invalid currency code!", align="center", font=("Arial", 20, "bold"))

# Run converter on click
turtle.listen()
screen.onclick(lambda x, y: convert())

# Initial message
writer.goto(0, 50)
writer.write("Click anywhere to start currency conversion!", align="center", font=("Arial", 16, "bold"))

# Keep window open


```
