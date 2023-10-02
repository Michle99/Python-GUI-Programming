import tkinter as tk
import random

root = tk.Tk()
root.title("Dice Roller")
root.geometry("300x300")
root.configure(background="white")

number_generated = tk.StringVar()
number_generated.set("1 to 6")

label = tk.Label(root, textvariable=number_generated, bg="white", fg="magenta", 
        font=("Tahoma", 25), pady=30
)
label.pack()

def roll():
    print("Rolling Dice...")
    number_generated.set(str(random.randint(1, 6)))
    
button = tk.Button(root, text="Roll", command=roll, bg="white", fg="brown",
        font=("Tahoma", 25),
        activebackground="#f79d27", activeforeground="#81f727",
        highlightbackground="#f79d27", highlightcolor="green"
)
button.pack()

root.mainloop()