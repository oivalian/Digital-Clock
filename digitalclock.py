import tkinter as tk
from time import strftime


def clock():
    string = strftime("%I:%M:%S %p")
    lbl.config(text=string)
    lbl.after(1000, clock)


def date():
    string = strftime("%A, %d %B %Y")
    title.config(text=string)
    lbl.after(1000, clock)


window = tk.Tk(className=" Clock")
window.config(background="#DAABEA")
window.geometry("480x240")
window.maxsize(3840, 2160)
window.minsize(480, 120)

title = tk.Label(window, font=("Arial", 25, "bold"), foreground="#5B5B5B", background="#DAABEA")
lbl = tk.Label(window, font=("Arial", 50, "bold"), foreground="#5B5B5B", background="#DAABEA")

title.pack()
lbl.pack()
date()
clock()
window.mainloop()
