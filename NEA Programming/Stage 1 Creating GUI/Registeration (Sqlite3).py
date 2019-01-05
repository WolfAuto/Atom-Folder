import sqlite3
import tkinter as tk
from tkinter import ttk


class MathsPro(tk.Tk): #Creating a class that inherits from tk.Tk

    def __init__(self, *args, **kwargs): # intialises the object
        tk.Tk.__init__(self, *args, **kwargs) #intialises the object as a tkinter frame

        # tk.Tk.iconbitmap(self, default="")
        tk.Tk.wm_title(self, "Maths Pro") # Sets the title of each page to be Maths Pro
        container = tk.Frame(self) # defined a container for all the framesto be kept

        container.pack(side="top", fill="both", expand=True) # The containter is filled with a bunch of frames

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1) # After the page being packed this allows it to be displayed correctly

        self.frames = {} # Empty dictionary where all the frames are kept

        for F in (Register, Register2): # contains all the pages being used #this will not work without pages

            frame = F(container, self) # Defines the frame from the for loop which contains all the pages

            self.frames[F] = frame  # Sets the top frame to be the current frame

            frame.grid(row=0, column=0, sticky="nsew") #This allows the frame to be displayed and streched

        self.show_frame(Register) # sets the first frame to be shown is a register page

    def show_frame(self, cont): # method that takes in cont as a controller

        frame = self.frames[cont] # Defines the frame from the chosen frame in the dictionary
        frame.tkraise() # Brings the frame to the top for the user to see


class Register(tk.Frame): #Creating a class that inheirts tk.Frame from tkinter

    def __init__(self, parent, controller): # intialise the class register with self, args and kwargs
        tk.Frame.__init__(self, parent) # intialise the frame with self and parent class
        tk.Frame.config(self) # allows the frame to be styled i.e changing background colour
        label = tk.Label(self, text="Registration 1", font=("Times New Roman", 50))
        label.pack(pady=10, padx=10)

        label_1 = tk.Label(self, text="First Name", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)

        label_a = tk.Label(self, text="Surname", width=20, font=("bold", 10))
        label_a.place(x=80, y=180)

        label_b = tk.Label(self, text="Age", width=20, font=("bold", 10))
        label_b.place(x=80, y=300)

        label_c = tk.Label(self, text="Class", width=20, font=("bold", 10))
        label_c.place(x=60, y=360)

        entry_c = tk.Entry(self)
        entry_c.place(x=240, y=360)

        entry_b = tk.Entry(self)
        entry_b.place(x=240, y=300)

        entry_2 = tk.Entry(self)
        entry_2.place(x=240, y=180)

        entry_1 = tk.Entry(self)
        entry_1.place(x=240, y=130)

        label_2 = tk.Label(self, text="Gender", width=20, font=("bold", 10))
        label_2.place(x=70, y=230)
        var = tk.IntVar()
        tk.Radiobutton(self, text="Male", padx=5, variable=var, value=1).place(x=205, y=230)
        tk.Radiobutton(self, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)


        label_3 = tk.Label(self, text="School", width=20, font=("bold", 10))
        label_3.place(x=70, y=420)

        var1 = tk.IntVar()
        tk.Radiobutton(self, text="Student", padx=5, variable=var1, value=1).place(x=205, y=420)
        if var1.get() == 1:
            var1="Student"
            print(var1.get())
        tk.Radiobutton(self, text="Teacher", padx=20, variable=var1, value=2).place(x=290, y=420)
        if var1.get() == 2:
            var1="Teacher"
            print(var1.get())
        button1= tk.Button(self, text="Enter details", command=lambda: controller.show_frame(Register2))
        button1.place(x=470, y=470)

class Register2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        label = tk.Label(self, text="Register 2", font=("Times New Roman", 50), bg="grey")
        label.pack(pady=10, padx=10)

        label_0 = tk.Label(self, text="Username", font=("Times New Roman", 20), bg="grey")
        label_0.pack()

        entry_0 = tk.Entry(self)
        entry_0.pack()

        label_1 = tk.Label(self, text="Password", bg="grey")
        label_1.pack()

        entry_1 = tk.Entry(self)
        entry_1.pack()

        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(Register))
        button1.pack()



root= MathsPro() # this runs the Maths Pro class
root.geometry("1280x800") # changes the size of the window
root.mainloop() # As MathsPro inherited from tkinter this function can be moved
