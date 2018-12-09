import tkinter as tk
from tkinter import ttk


class MathsPro(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="")
        tk.Tk.wm_title(self, "Maths Pro")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Start Page", font=("Times New Roman", 20))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page 1",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Visit Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Reigstration Form 1", font=("Times New Roman", 50))
        label.pack(pady=10, padx=10)

        label_0 = tk.Label(self, text="Reigstration Form 1", width=20, font=("bold", 10))
        label_0.place(x=90, y=53)

        label_1 = tk.Label(self, text="First Name", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)

        label_a = tk.Label(self, text="Surname", width=20, font=("bold", 10))
        label_a.place(x=75, y=180)

        entry_a = tk.Entry(self)
        entry_a.place(x=240, y=180)

        entry_1 = tk.Entry(self)
        entry_1.place(x=240, y=130)

        label_2 = tk.Label(self, text="Gender", width=20, font=("bold", 10))
        label_2.place(x=70, y=230)
        var = tk.IntVar()
        tk.Radiobutton(self, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
        tk.Radiobutton(self, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)
        label_b = tk.Label(self, text="Student or Teacher", width=20, font=("bold", 10))
        label_b.place(x=70, y=280)
        var1 = tk.IntVar()
        tk.Radiobutton(self, text="Student", padx=3, variable=var1, value=1).place(x=235, y=280)
        tk.Radiobutton(self, text="Teacher", padx=20, variable=var1, value=2).place(x=300, y=280)
        button1 = ttk.Button(self, text="Back to home", width=50,
                             command=lambda: controller.show_frame(MainMenu))
        button1.place(x=500, y=600)

        button2 = ttk.Button(self, text="Visit page two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Visit page three",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=("Times New Roman", 20))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(MainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Visit page one",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Three Graph Page",
                         font=("Times New Roman", 20))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(MainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Visit page one",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()


root = MathsPro()
root.geometry("1000x1000")
root.mainloop()
