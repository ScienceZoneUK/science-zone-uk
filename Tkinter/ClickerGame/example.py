import tkinter
from time import strftime

root = tkinter.Tk()
root.title("Clicker Game")
root.geometry("800x600")
root.resizable(False, False)

count = 0
autoclickers = 0

def buttonPressed():
    global count
    count += 1
    count_label.config(text = count)
    
def autoclick():
    global count
    count += 1
    count_label.config(text = count)
    count_label.after(1000, autoclick)
    
def buyAutoclicker():
    global count
    if (count >= 10):
        count -= 10
        count_label.config(text = count)
        global autoclickers
        autoclickers += 1
        autoclicker_button.config(text = "buy autoclicker (" + str(autoclickers) + ")")
        count_label.after(1000, autoclick)

count_label = tkinter.Label(
    root,
    font = ("Arial", 48, "bold"),
    bg = "black",
    fg = "lime",
    padx = 20,
    pady = 20
)
count_label.pack(fill = "both", expand = False)
count_label.config(text = count)

click_button = tkinter.Button(
    root,
    font = ("Arial", 48, "bold"),
    bg = "black",
    fg = "lime",
    padx = 20,
    pady = 20,
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
    pady = 20,
    command = buyAutoclicker
)
autoclicker_button.pack(fill = "both", expand = False)
autoclicker_button.config(text = "buy autoclicker (" + str(autoclickers) + ")")
    
root.mainloop()
