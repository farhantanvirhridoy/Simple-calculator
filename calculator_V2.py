from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.configure(bg='#1B202D')

display = Entry(root, borderwidth=5,width=22,font="Cambria 18",bg='#434B65')
display.grid(row=0,column=0,columnspan=4)

global next_clear
next_clear = False

def button_click(number):
    global next_clear
    if next_clear: 
        clear()
        next_clear = False
    prev = display.get()
    clear()
    display.insert(0, str(prev) + str(number))


def clear():
    display.delete(0, END)

def calculation():
    global next_clear
    next_clear = True
    global first
    global opr
    sec = display.get()
    if opr == "+":
        result = int(first) + int(sec)
    elif opr == "-":
        result = int(first) - int(sec) 
    elif opr == "*":
        result = int(first) * int(sec)
    elif opr == "/":
        result = int(first) / int(sec) 
    clear()
    display.insert(0, str(first)+opr+str(sec)+'='+str(result))
    
    

def plus():
    global first
    global opr
    first = display.get()
    clear()
    opr = "+"

def minus():
    global first
    global opr 
    first = display.get()
    clear()
    opr = "-"

def mult():
    global first
    global opr
    first = display.get()
    clear()
    opr = "*"

def div():
    global first
    global opr
    first = display.get()
    clear()
    opr = "/"

button_1 = Button(root,text="1",padx=20,pady=15,activebackground="#1B202D", bg="#2D3243",fg="white", font="Cambria 16", command= lambda: button_click(1))
button_2 = Button(root,text="2",padx=20,pady=15,activebackground="#1B202D",bg="#2D3243",fg="white", font="Cambria 16", command= lambda: button_click(2))
button_3 = Button(root,text="3",padx=20,pady=15,activebackground="#1B202D",bg="#2D3243",fg="white", font="Cambria 16", command= lambda: button_click(3))
button_4 = Button(root,text="4",padx=20,pady=15,activebackground="#1B202D", bg="#2D3243",fg="white",font="Cambria 16", command= lambda: button_click(4))
button_5 = Button(root,text="5",padx=20,pady=15,activebackground="#1B202D",bg="#2D3243",fg="white", font="Cambria 16", command= lambda: button_click(5))
button_6 = Button(root,text="6",padx=20,pady=15,activebackground="#1B202D",bg="#2D3243",fg="white", font="Cambria 16", command= lambda: button_click(6))
button_7 = Button(root,text="7",padx=20,pady=15,activebackground="#1B202D",bg="#2D3243",fg="white", font="Cambria 16", command= lambda: button_click(7))
button_8 = Button(root,text="8",padx=20,pady=15,activebackground="#1B202D",bg="#2D3243",fg="white", font="Cambria 16", command= lambda: button_click(8))
button_9 = Button(root,text="9",padx=20,pady=15,activebackground="#1B202D", bg="#2D3243",fg="white",font="Cambria 16", command= lambda: button_click(9))
button_0 = Button(root,text="0",padx=20,pady=15,activebackground="#1B202D",bg="#2D3243",fg="white", font="Cambria 16", command= lambda: button_click(0))
button_clear = Button(root,text="clear",padx=4,pady=15,activebackground="#1B202D",bg="#2D3243",fg="white", font="Cambria 16", command=clear)
button_equal = Button(root,text="=",padx=20,pady=15,activebackground="#1B202D",bg="#2D3243",fg="white", font="Cambria 16", command=calculation)
button_plus = Button(root,text="+",padx=19,pady=15,activebackground="#1B202D",bg="#2D3243",fg="white", font="Cambria 16", command=plus)
button_minus = Button(root,text="-",padx=20,pady=15,activebackground="#1B202D",bg="#2D3243",fg="white", font="Cambria 16",command=minus)
button_mult = Button(root,text="*",padx=20,pady=15,activebackground="#1B202D",bg="#2D3243",fg="white", font="Cambria 16",command=mult)
button_div = Button(root,text="/",padx=19,pady=15,activebackground="#1B202D", bg="#2D3243",fg="white",font="Cambria 16",command=div)





button_1.grid(row=3,column=0,padx=5,pady=5)
button_2.grid(row=3,column=1,padx=5,pady=5)
button_3.grid(row=3,column=2,padx=5,pady=5)
button_mult.grid(row=3,column=3,padx=5,pady=5)

button_4.grid(row=2,column=0,padx=5,pady=5)
button_5.grid(row=2,column=1,padx=5,pady=5)
button_6.grid(row=2,column=2,padx=5,pady=5)
button_minus.grid(row=2,column=3,padx=5,pady=5)

button_7.grid(row=1,column=0,padx=5,pady=5)
button_8.grid(row=1,column=1,padx=5,pady=5)
button_9.grid(row=1,column=2,padx=5,pady=5)
button_plus.grid(row=1,column=3,padx=5,pady=5)

button_0.grid(row=4,column=0,padx=5,pady=5)
button_clear.grid(row=4,column=1,padx=5,pady=5)
button_equal.grid(row=4,column=2,padx=5,pady=5)
button_div.grid(row=4,column=3,padx=5,pady=5)

root.mainloop()