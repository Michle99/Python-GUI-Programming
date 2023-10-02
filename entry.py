import tkinter as tk

window = tk.Tk()
frame1 = tk.Frame()
frame1.pack()

ent_name = tk.Entry(master=frame1, width=40, bg="black", fg="red")
ent_name.pack()
ent_name.insert(0, "What is your name?")

window.mainloop()