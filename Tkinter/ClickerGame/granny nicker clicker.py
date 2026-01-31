#granny nicker clicker will be the best its your job to improve it (dan)

import tkinter
from time import strftime

root = tkinter.Tk()
root.title("Clicker Game")
root.geometry("800x600")
root.resizable(False, False)

count = 0
autoclickers = 0
clickpower = 1
autoclickersadvanced = 0

def buttonPressed():
    global count
    global clickpower
    count += clickpower
    count_label.config(text = count)
    
def autoclick():
    global count
    count += 1
    count_label.config(text = count)
    count_label.after(1000, autoclick)
    
def autoclickadvanced():
    global count
    count += 75
    count_label.config(text = count)
    count_label.after(1000, autoclickadvanced)
    
def buyAutoclicker():
    global count
    if (count >= 10):
        count -= 10
        count_label.config(text = count)
        global autoclickers
        autoclickers += 1
        autoclicker_button.config(text = "buy autoclicker (" + str(autoclickers) + ")")
        count_label.after(1000, autoclick)
        
def buyPowerincrease():
    global count
    if (count >= 50):
        count -= 50
        count_label.config(text = count)
        global clickpower
        clickpower += 1
        powerincrease_button.config(text = "buy power (" + str(clickpower) + ")")
        
def buyAutoclickerAdvanced():
    global count
    if (count >= 780):
        count -= 780
        count_label.config(text = count)
        global autoclickersadvanced
        autoclickersadvanced += 1
        autoclickeradvanced_button.config(text = "buy autoclickeradvanced (" + str(autoclickersadvanced) + ")")
        count_label.after(1000, autoclickadvanced)
        
    

count_label = tkinter.Label(
    root,
    font = ("Arial", 48, "bold"),
    bg = "black",
    fg = "lime",
    padx = 20,
    pady = 10
)
count_label.pack(fill = "both", expand = False)
count_label.config(text = count)

click_button = tkinter.Button(
    root,
    font = ("Arial", 48, "bold"),
    bg = "black",
    fg = "lime",
    padx = 20,
    pady = 10,
    command = buttonPressed
)
click_button.pack(fill = "both", expand = False)
click_button.config(text = "click")

autoclicker_button = tkinter.Button(
    root,
    font = ("Arial", 48, "bold"),
    bg = "black",
    fg = "lime",
    padx = 20,
    pady = 10,
    command = buyAutoclicker
)
autoclicker_button.pack(fill = "both", expand = False)
autoclicker_button.config(text = "buy autoclicker (" + str(autoclickers) + ")")

powerincrease_button = tkinter.Button(
    root,
    font = ("Arial", 48, "bold"),
    bg = "black",
    fg = "lime",
    padx = 20,
    pady = 10,
    command = buyPowerincrease
)
powerincrease_button.pack(fill = "both", expand = False)
powerincrease_button.config(text = "buy power (" + str(clickpower) + ")")

autoclickeradvanced_button = tkinter.Button(
    root,
    font = ("Arial", 48, "bold"),
    bg = "black",
    fg = "lime",
    padx = 20,
    pady = 10,
    command = buyAutoclickerAdvanced
)
autoclickeradvanced_button.pack(fill = "both", expand = False)
autoclickeradvanced_button.config(text = "buy autoclickeradvanced (" + str(autoclickersadvanced) + ")")


root.mainloop()
