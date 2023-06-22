import tkinter as tk
import time 
from datetime import date

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    current_day = date.today().strftime("%A")
    clock_label1.config(text=current_time)
    day_label1.config(text=current_day)
    clock_label1.after(1000, time)

#creat the main window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("300x100")
window.configure(bg="white")

#creating label
clock_label1 =tk.Label(window, font=("Helvetica", 30), fg="red", bg="white")
clock_label1.pack(pady=5)

day_label1 = tk.Label(window, font=("Helvetica", 20), fg="black", bg="white")
day_label1.pack()

update_time()
#start the main loop
window.mainloop()


