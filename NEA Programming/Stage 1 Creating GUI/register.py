import tkinter as tk
root = tk.Tk()
root.geometry('500x500')
root.title("Maths Pro - Registration Form 1")

label_0 = tk.Label(root, text="Reigstration Form 1", width=20, font=("bold", 10))
label_0.place(x=90, y=53)

label_1 = tk.Label(root, text="First Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = tk.Entry(root)
entry_1.place(x=240, y=130)

label_2 = tk.Label(root, text="Gender", width=20, font=("bold", 10))
label_2.place(x=70, y=230)
var = tk.IntVar()
tk.Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
tk.Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)
root.mainloop()
