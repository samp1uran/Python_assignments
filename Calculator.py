#step 1 (import)
from tkinter import *
#step 2 (gui intraction)
window = Tk()
window.geometry("250x250")
#step 3 (inputs)
    #Entry Box
e = Entry(window, width = 100 , borderwidth = 5)
e.place(x = 0, y = 0)
#Buttons
def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0, str(result) + str(num))


b = Button(window , text = "1", width = 6, command = lambda:click(1))
b.place(x = 10, y = 60)
b = Button(window , text = "2", width = 6, command = lambda:click(2))
b.place(x = 70, y = 60)
b = Button(window , text = "3", width = 6, command = lambda:click(3))
b.place(x = 130, y = 60)
#definning a function 
def mul():
    n1 = e.get()
    global math 
    math = "multipication"
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window , text = "*", width = 6, command = mul)
b.place(x = 190, y = 60)
b = Button(window , text = "4", width = 6, command = lambda:click(4))
b.place(x = 10, y = 100)
b = Button(window , text = "5", width = 6, command = lambda:click(5))
b.place(x = 70, y = 100)
b = Button(window , text = "6", width = 6, command = lambda:click(6))
b.place(x = 130, y = 100)
#definning a function 
def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window , text = "/", width = 6, command =div)
b.place(x = 190, y = 100)
b = Button(window , text = "7", width = 6, command = lambda:click(7))
b.place(x = 10, y = 140)
b = Button(window , text = "8", width = 6, command = lambda:click(8))
b.place(x = 70, y = 140)
b = Button(window , text = "9", width = 6, command = lambda:click(9))
b.place(x = 130, y = 140)
#definning a function 
def mod():
    n1 = e.get()
    global math
    math = "module"
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window , text = "%", width = 6, command = mod)
b.place(x = 190, y = 140)
b = Button(window , text = "0", width = 6, command = lambda:click(0))
b.place(x = 10, y = 180)
#definning a function 
def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window , text = "+", width = 6, command = add)
b.place(x = 70, y = 180)
#definning a function 
def min():
    n1 = e.get()
    global math
    math = "minus"
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window , text = "-", width = 6, command = min)
b.place(x = 130, y = 180)
#definning a function 
def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,i + int(n2))
    elif math == "minus":
        e.insert(0,i - int(n2))
    elif math == "multipication":
        e.insert(0,i * int(n2))
    elif math == "division":
        e.insert(0,i / int(n2))


b = Button(window , text = "=", width = 6, command = equal)
b.place(x = 190, y = 180)
#definning a function 
def clear():
    e.delete(0,END)
    
b = Button(window , text = "Clear", width = 6, command = clear)
b.place(x = 90, y = 210)
#step 4 (mainloop)
mainloop()