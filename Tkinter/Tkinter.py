from tkinter import*
# label1=Label(root, text="Name") #Put a label on Tkinter

# label1.grid(row=0,column=0, sticky="E") #Grid function

#label3=Label(root, text="Password:")

#label3.grid(row=1,column=0, sticky="E")

# entrySpace= Entry(root)#use the Entry(root) to make an entry for the user

# entrySpace.grid(row=0,column=1)

# entrySpace2= Entry(root)#use the Entry(root) to make an entry for the user

# entrySpace2.grid(row=1,column=1)


#cbutton= Checkbutton(root, text="Remember Password:")

# cbutton.grid(columnspan=2)


#cbutton= Checkbutton(root, text="Male")

# cbutton.grid(row=1,column=1)

#cbutton= Checkbutton(root, text="Female")

# cbutton.grid(row=1,column=2)
# button1=Button(root, text="Click Me") #use the command function to link a function to a button
# button1.bind("<Button-1>",printName)

# button1.pack()
root = Tk()  # initalise Tkinter


def printName(event):
    print("Hello World")


def leftClick(event):
    print("Left")


def rightClick(event):
    print("Right")


def leftKey(event):
    print("Left Key pressed")


def rightKey(event):
    print("Right Key pressed")


root.geometry("500x500")

root.bind("<Button-1>", leftClick)
root.bind("<Button-2>", rightClick)
root.bind("<Left>", leftKey)
root.bind("<Right>", rightKey)

root.mainloop()
