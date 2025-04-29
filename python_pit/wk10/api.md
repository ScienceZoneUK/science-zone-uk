# Finding api's

Search for fun apis to test your skills in using them!
[List of api's](https://github.com/public-apis/public-apis)

## Raw endpoints
[Dog facts](https://dogapi.dog/api/v2/facts)    
[Bank Holidays](https://www.gov.uk/bank-holidays.json)     

------   
[Carbon Intensity API](https://api.carbonintensity.org.uk/intensity)   
National Energy System Operator (NESO), in partnership with Environmental Defense Fund Europe, University of Oxford Department of Computer Science and WWF, have developed the world's first Carbon Intensity forecast with a regional breakdown.
The Carbon Intensity API uses state-of-the-art Machine Learning and sophisticated power system modelling to forecast the carbon intensity and generation mix 96+ hours ahead for each region in Great Britain.
Our OpenAPI allows consumers and smart devices to schedule and minimise COz emissions at a local level.


------- 
[Currencies-GBP](https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/gbp.json)






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

#Save the response into a dictionary
data = response.json()

#Print the data
print(data)

#get the exchange rate
rate = data["gbp"]["eur"]

#Print the exchange rate
print(rate)

```

- Step through the code and understand it
- Modify the conversion 'gbp' to .....?
- If you enter the wrong currency, what's the error?
- Write a try and except to catch the error and print a meaningful message



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
