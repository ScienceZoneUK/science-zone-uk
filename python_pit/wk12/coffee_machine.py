# coffee_machine.py

class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 1000,
            "milk": 800,
            "coffee": 500
        }
        self.menu = {
            "espresso": {"price": 2.0, "water": 50, "milk": 0, "coffee": 18},
            "latte": {"price": 2.5, "water": 200, "milk": 150, "coffee": 24},
            "cappuccino": {"price": 3.0, "water": 250, "milk": 100, "coffee": 24},
            "flat white": {"price": 2.8, "water": 150, "milk": 100, "coffee": 20},
            "mocha": {"price": 3.5, "water": 200, "milk": 150, "coffee": 22}
        }

    def print_menu(self):
        print("☕ Coffee Menu:")
        for coffee, info in self.menu.items():
            print(f"- {coffee.title()}: £{info['price']}")

    def check_resources(self, drink):
        for item in ["water", "milk", "coffee"]:
            if self.resources[item] < self.menu[drink][item]:
                print(f"❌ Sorry, not enough {item}.")
                return False
        return True

    def process_payment(self, cost):
        print("💰 Please insert coins.")
        total = 0
        total += int(input("How many £1 coins? ")) * 1.0
        total += int(input("How many 50p coins? ")) * 0.5
        total += int(input("How many 20p coins? ")) * 0.2
        total += int(input("How many 10p coins? ")) * 0.1
        total = round(total, 2)

        if total < cost:
            print("❌ Not enough money. Money refunded.")
            return False
        change = round(total - cost, 2)
        print(f"✅ Payment accepted. Your change is £{change}.")
        return True

    def make_coffee(self, drink):
        for item in ["water", "milk", "coffee"]:
            self.resources[item] -= self.menu[drink][item]
        print(f"☕ Here is your {drink}. Enjoy!")
