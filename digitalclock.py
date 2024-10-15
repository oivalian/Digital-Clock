import tkinter as tk
from time import strftime

def clock():
    time = strftime("%A, %d %B %Y\n\n%I:%M:%S %p")
    time_label.config(text=time)
    time_label.after(1000, clock)

root = tk.Tk()
root.config(background="#0d1117")
root.title("Digital Clock")
root.resizable(False, False)

time_label = tk.Label(root, font="Arial 25 bold", fg="#ffffff", bg="#0d1117")

clock()
time_label.pack(pady=20, padx=20)
root.mainloop()
