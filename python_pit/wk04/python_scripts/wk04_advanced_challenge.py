# Week 4 Advanced Challenge: Python Basics with Decision Making
# Instructions:
# 1.
# 2.
# 3. 


import time

shop = ["Pears", "Apples", "Bananas"]
end = False

while (end != True):

    print("Welcome to your own Tesco store!")
    time.sleep(1)
    print("Currently in stock: ")
    for item in shop:
      print(item)
      time.sleep(0.3)
      
    choice = input("Add, delete or sort your shop's stock").lower()

    if choice == "add":
        item = input("What item do you want to add to your shop?")
        shop.append(item)
        print(item + " is now in your basket.")
        time.sleep(1)
      
    elif choice == "delete":
        item = input("What item do you want to delete from your shop?")
        if shop.count(item) > 0:
            shop.remove(item)
            print(item + " has been removed from your shop.")
            time.sleep(1)
        else:
            print(item + " is not in your shop.")
            time.sleep(1)

    elif choice == "sort":
        print("Sorting into Alphabetical Order...")
        shop.sort()
        time.sleep(1)
        checkout = input("Shop has been sorted, have you completed your tasks? Y/N").lower()
        if checkout == "y":
          end = True
        
    else:
        print("Please write the commands, add, delete or sort")

print("Thanks for shopping with us!")
