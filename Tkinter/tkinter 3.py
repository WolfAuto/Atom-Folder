from tkinter import *

root=Tk()

equa = ""
store=""

equation = StringVar()
calculation= Label(root,textvariable=equation)

equation.set("Enter your Equation")

calculation.grid(columnspan=4)


def btnPress(num):
    global equa
    equa= equa+ str(num)
    equation.set(equa)
def EqualPress():
    global equa
    total=eval(equa)
    equation.set(total)
    equa=""
def Clear():
    global equa
    equa=""
    equation.set("")
button1=Button(root, text="1",command=lambda:btnPress(1))
button1.grid(row=1,column=0)
button2=Button(root, text="2",command=lambda:btnPress(2))
button2.grid(row=1,column=1)
button3=Button(root, text="3",command=lambda:btnPress(3))
button3.grid(row=1,column=2)
button4=Button(root, text="4",command=lambda:btnPress(4))
button4.grid(row=2,column=0)
button5=Button(root, text="5",command=lambda:btnPress(5))
button5.grid(row=2,column=1)
button6=Button(root, text="6",command=lambda:btnPress(6))
button6.grid(row=2,column=2)
button7=Button(root, text="7",command=lambda:btnPress(7))
button7.grid(row=3,column=0)
button8=Button(root, text="8",command=lambda:btnPress(8))
button8.grid(row=3,column=1)
button9=Button(root, text="9",command=lambda:btnPress(9))
button9.grid(row=3,column=2)
button0=Button(root, text="0",command=lambda:btnPress(0))
button0.grid(row=4,column=2)
Plus=Button(root, text="+",command=lambda:btnPress("+"))
Plus.grid(row=1,column=3)
Minus=Button(root, text="-",command=lambda:btnPress("-"))
Minus.grid(row=1,column=4)
Multiply=Button(root, text="*",command=lambda:btnPress("*"))
Multiply.grid(row=2,column=3)
Divide=Button(root, text="/",command=lambda:btnPress("/"))
Divide.grid(row=2,column=4)
Equal=Button(root, text="=", command=EqualPress)
Equal.grid(row=3,column=4)
Clear=Button(root, text="C", command=Clear)
Clear.grid(row=3,column=3)

root.mainloop()
