from tkinter import HIDDEN, NORMAL, Tk, Canvas

def toggle_eyes():
    current_color = c.itemcget(left_eye, "fill")
    new_color = c.body_color if current_color == "white" else "white"
    current_state = c.itemcget(left_pupil, "state")
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(left_pupil, state=new_state)
    c.itemconfigure(right_pupil, state=new_state)
    c.itemconfigure(left_eye, fill=new_color)
    c.itemconfigure(right_eye, fill=new_color)
    
def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(2000, blink)

root = Tk()
c = Canvas(root, width=400, height=400)
c.configure(bg="dark blue", highlightthickness=0)

c.body_color = "SkyBlue1"

body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)

left_ear = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
right_ear = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)

left_foot = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
right_foot = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)

left_eye = c.create_oval(130, 110, 160, 170, outline="black", fill="white")
left_pupil = c.create_oval(140, 145, 150, 155, outline="black", fill="black")
right_eye = c.create_oval(230, 110, 260, 170, outline="black", fill="white")
right_pupil = c.create_oval(240, 145, 250, 155, outline="black", fill="black")

mouth = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)


c.pack()
root.after(1000, blink)
root.mainloop()
