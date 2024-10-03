# Week 4 Challenge: Lists and Arrays
# Instructions:
# 1.
# 2. 
# 3. 

import time

shop = ["Apples", "Chicken", "Pasta", "Canned Tomatoes", "Milk", "Bread", "Eggs", "Lawnmower", "Switch Game", "Dinosaur Egg"]
basket = []
end = False

while (end != True):

    print("Welcome to Tesco!")
    time.sleep(1)
    print("Currently in stock: ")
    for item in shop:
      print(item)
      time.sleep(0.3)
      
    choice = input("Add, delete or view your basket").lower()

    if choice == "add":
        item = input("What item do you want to add to your basket?")
        if shop.count(item) > 0:
          basket.append(item)
          print(item + " is now in your basket.")
          time.sleep(1)
        else:
          print(item + " is currently not in stock.")
          time.sleep(1)
      
    elif choice == "delete":
        item = input("What item do you want to delete from your basket?")
        if basket.count(item) > 0:
          basket.remove(item)
          print(item + " has been removed your basket.")
          time.sleep(1)
        else:
          print(item + " is not in your basket.")
          time.sleep(1)

    elif choice == "view":
        print("Your basket contains: ")
        for item in basket:
          print(item)
          time.sleep(0.3)
        checkout = input("Would you like to checkout? Y/N").lower()
        if checkout == "y":
          end = True
        
    else:
        print("Please write the commands, add, view or delete")

print("Thanks for shopping with us!")
