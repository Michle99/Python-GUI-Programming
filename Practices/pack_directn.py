import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, height=100, bg="green")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, height=50, bg="purple")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, height=25, bg="pink")
frame3.pack(fill=tk.X)

window.mainloop()