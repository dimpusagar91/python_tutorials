import Tkinter as tk
from Tkinter import *
import tkMessageBox
root = Tk()
buttons = {}
signVal = ''
firstVal = 1
root.title('Calculator')
root.attributes("-toolwindow", 1)
def createNumbers():
    global buttons
    buttonNum = 0
    for b in range( 2 ):
        for b2 in range( 5 ):
            button = Button(frame2, text = buttonNum, font = "Courier 9", width = 5, bd = 3 )
            button.grid(row=b, column=b2)
            buttons[ button ] = buttonNum
            buttonNum += 1
            button.bind( "<Button-1>", makeChoice )
def operators():
    button = Button(frame2, text = '+', font = "Courier 9", width = 5, bd = 3, command = lambda : operation('+') )
    button.grid(row=2, column=0)
    button = Button(frame2, text = '-', font = "Courier 9", width = 5, bd = 3, command = lambda : operation('-') )
    button.grid(row=2, column=1)
    button = Button(frame2, text = '*', font = "Courier 9", width = 5, bd = 3, command = lambda : operation('*') )
    button.grid(row=2, column=2)
    button = Button(frame2, text = '/', font = "Courier 9", width = 5, bd = 3, command = lambda : operation('/') )
    button.grid(row=2, column=3)
    button = Button(frame2, text = '=', font = "Courier 9", width = 5, bd = 3, command = lambda : excutionPart('=') )
    button.grid(row=2, column=4)
    button = Button(frame2, text = 'Clear', font = "Courier 9", width = 5, bd = 3, command = lambda : clearAll('clear') )
    button.grid(row=3, column=0)
def makeChoice( event ):
    global buttons    
    if (v.get() is None) or (len(v.get()) == 0):
       v.set(buttons[ event.widget ])       
    else:
        v.set(str(v.get())+str(buttons[ event.widget ]))
def operation(value):
    try:        
        global signVal
        global firstVal
        signVal = value
        if not isinstance(v.get(), int):
            firstVal = int(v.get())
        else:
            tkMessageBox.showerror("Error","Wrong Formate")
        print "First Value :", firstVal
        v.set('')
    except TypeError:
        tkMessageBox.showerror("Error","Wrong Formate")
def excutionPart(ex):
    print "Second Value :", str(v.get())
    if signVal is '+':
        v.set(int(firstVal)+int(v.get()))
    elif signVal is '-':
        v.set(int(firstVal)-int(v.get()))
    elif signVal is '*':
        v.set(int(firstVal)*int(v.get()))
    elif signVal is '/':
        v.set(int(firstVal)/int(v.get()))
    else:
        v.set('')
    print "Result is :", str(v.get())
def clearAll(val):
    v.set('')
#Top Frame 
frame1 = Frame(root)
frame1.pack(side = TOP)
#Bottom Frame 
frame2 = Frame(root)
frame2.pack(side = BOTTOM)
v = StringVar()
e = Entry(frame1, textvariable=v, width = 30)
e.pack(side = LEFT)
createNumbers()
operators()
root.mainloop()