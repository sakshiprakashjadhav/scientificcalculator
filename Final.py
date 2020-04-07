from tkinter import *
import math
import parser
import tkinter.messagebox
from functools import reduce
root = Tk()
root.title("CALCULATOR")
root.configure(background="black")
root.resizable(width=False, height=False)
root.geometry("285x305+0+0")

calc=Frame(root)
calc.grid()

op = ""
text = tkinter.StringVar()


def btn_press(num):
	global op
	op = op+ str(num)
	text.set(op)
   

def clear():
    global op
    op = ""
    text.set("")


'''
def equal():
    try:
        global op
        total = str(eval(op))
        text.set(total)
        op = ""


    except:
        text.set("Error")
        op = ""

'''

def delete():
    try:
        global op
        expression=text.get()
        result = expression[:-1]
        text.set(result)
    except:
        text.set("error")
        op=" "

def fix():
    try:
        global op
        total = text.get()
        text.set('%.2f' %float(total))
        print(total)
        op=" "
    except:
        text.set("error")
        op=" "

def sci():
    try:
        global op
        total = text.get()
        text.set('%.2f' %float(total))
        print(total)
        op=" "
    except:
        text.set("error")
        op=" "

def equal():
    try:
        global op
        total = str(eval(op))
        text.set(total)
        if "0b" in total or "0x" in total or "0o" in total:
        	text.set(total[2:])#for removing prefix 
        print(total)

        
        #op = ""

    except:

        if 'c' in op:
            s = op.find('c')
            i = int(op[:s])
            ii = int(op[1 + s:])
            if i >= ii:
                a = math.factorial(i)
                b = math.factorial(ii) * math.factorial(i - ii)
                text.set(a / b)
                op = ""
            else:
                text.set("N must be greater then R")

        if 'p' in op:
            s1 = op.find('p')
            print(s1)
            i1 = int(op[:s1])
            ii1 = int(op[1 + s1:])
            if i1 >= ii1:
                a1 = math.factorial(i1)
                b1 = math.factorial(i1 - ii1)
                text.set(a1 / b1)
                op = ""
            else:
                text.set("N must be greater then R")
                op = ""


        lst = ['c', 'p']
        if not 'c' in op or 'p' in op:
            text.set("Error")
        op = ""

#**********************************************FIELD*************************************************#



	

field = tkinter.Entry(root, font=("Arial", 11, "bold"), textvariable=text, width=35).grid(row=2, column=0, columnspan=5)

#*****************************************STANDARD****************************************************#

btn1 = tkinter.Button(root, font=("Arial", 11, "bold"), text="1", width=6, height=2, bd=5,
                      command=lambda: btn_press(1)).grid(row=3, column=1)
btn2 = tkinter.Button(root, font=("Arial", 11, "bold"), text="2", width=6, height=2, bd=5,
                      command=lambda: btn_press(2)).grid(row=3, column=2)
btn3 = tkinter.Button(root, font=("Arial", 11, "bold"), text="3", width=6, height=2, bd=5,
                      command=lambda: btn_press(3)).grid(row=3, column=3)
btn4 = tkinter.Button(root, font=("Arial", 11, "bold"), text="+", width=6, height=2, bd=5, bg="green",
                      command=lambda: btn_press("+")).grid(row=3, column=4)
btn5 = tkinter.Button(root, font=("Arial", 11, "bold"), text="4", width=6, height=2, bd=5,
                      command=lambda: btn_press(4)).grid(row=4, column=1)
btn6 = tkinter.Button(root, font=("Arial", 11, "bold"), text="5", width=6, height=2, bd=5,
                      command=lambda: btn_press(5)).grid(row=4, column=2)
btn7 = tkinter.Button(root, font=("Arial", 11, "bold"), text="6", width=6, height=2, bd=5,
                      command=lambda: btn_press(6)).grid(row=4, column=3)
btn8 = tkinter.Button(root, font=("Arial", 11, "bold"), text="-", width=6, height=2, bd=5, bg="green",
                      command=lambda: btn_press("-")).grid(row=4, column=4)
btn9 = tkinter.Button(root, font=("Arial", 11, "bold"), text="7", width=6, height=2, bd=5,
                      command=lambda: btn_press(7)).grid(row=5, column=1)
btn10 = tkinter.Button(root, font=("Arial", 11, "bold"), text="8", width=6, height=2, bd=5,
                       command=lambda: btn_press(8)).grid(row=5, column=2)
btn11 = tkinter.Button(root, font=("Arial", 11, "bold"), text="9", width=6, height=2, bd=5,
                       command=lambda: btn_press(9)).grid(row=5, column=3)
btn12 = tkinter.Button(root, font=("Arial", 11, "bold"), text="*", width=6, height=2, bd=5, bg="green",
                       command=lambda: btn_press("*")).grid(row=5, column=4)
btn13 = tkinter.Button(root, font=("Arial", 11, "bold"), text="√", width=6, height=2, bd=5,
                       command=lambda: btn_press(math.sqrt(int(text.get())))).grid(row=6,column=1)
btn14 = tkinter.Button(root, font=("Arial", 11, "bold"), text="0", width=6, height=2, bd=5,
                       command=lambda: btn_press(0)).grid(row=6, column=2)
btn15 = tkinter.Button(root, font=("Arial", 11, "bold"), text="=", width=6, height=2, bd=5,
                       command=lambda: equal()).grid(row=6, column=3)
btn16 = tkinter.Button(root, font=("Arial", 11, "bold"), text="/", width=6, height=2, bd=5, bg="green",
                       command=lambda: btn_press("/")).grid(row=6, column=4)
btn17 = tkinter.Button(root, font=("Arial", 11, "bold"), text="(", width=6, height=2, bd=5, bg="green",
                       command=lambda: btn_press('(')).grid(row=7, column=1)
btn18 = tkinter.Button(root, font=("Arial", 11, "bold"), text=")", width=6, height=2, bd=5, bg="green",
                       command=lambda: btn_press(')')).grid(row=7, column=2)
btn19 = tkinter.Button(root, font=("Arial", 11, "bold"), text="c", width=6, height=2, bd=5, bg="green",
                       command=lambda: clear()).grid(row=7, column=3)
btn20 = tkinter.Button(root, font=("Arial", 11, "bold"), text="del", width=6, height=2, bd=5, bg="green",
                       command=lambda: delete()).grid(row=7, column=4)




#*************************************************SCIENTIFIC****************************************************************************#



lbl = tkinter.Label(root, text="Scientific Calculator", font=("Arial", 11, "bold"), width=34).grid(row=2, column=5, columnspan=5)
btn21 = tkinter.Button(root, font=("Arial", 11, "bold"), text="bin", width=7, height=2, bd=5, bg="green",
                      command=lambda: btn_press("bin(") ).grid(row=3, column=5)
btn22 = tkinter.Button(root, font=("Arial", 11, "bold"), text="oct", width=7, height=2, bd=5, bg="green",
                      command=lambda: btn_press("oct(")).grid(row=3, column=6)
btn23 = tkinter.Button(root, font=("Arial", 11, "bold"), text="hex", width=7, height=2, bd=5, bg="green",
                      command=lambda: btn_press("hex(")).grid(row=3, column=7)
btn24 = tkinter.Button(root, font=("Arial", 11, "bold"), text="π", width=7, height=2, bd=5, bg="green",
                      command=lambda: btn_press('3.14')).grid(row=3,column=8)
btn25 = tkinter.Button(root, font=("Arial", 11, "bold"), text="sin", width=7, height=2, bd=5, bg="green",
                     command=lambda: btn_press("sin(")).grid(row=4, column=5)
btn26 = tkinter.Button(root, font=("Arial", 11, "bold"), text="cos", width=7, height=2, bd=5, bg="green",
                     command=lambda: btn_press("cos(")).grid(row=4, column=6)
btn27 = tkinter.Button(root, font=("Arial", 11, "bold"), text="tan", width=7, height=2, bd=5, bg="green",
                     command=lambda: btn_press("tan(")).grid(row=4, column=7)
btn28 = tkinter.Button(root, font=("Arial", 11, "bold"), text="x^2", width=7, height=2, bd=5, bg="green",
                     command=lambda: btn_press("**2")).grid(row=4, column=8)
btn29 = tkinter.Button(root, font=("Arial", 11, "bold"), text="log", width=7, height=2, bd=5, bg="green",
                     command=lambda: btn_press("log(")).grid(row=5, column=5)
btn30 = tkinter.Button(root, font=("Arial", 11, "bold"), text="log2", width=7, height=2, bd=5, bg="green",
                     command=lambda:btn_press("log2(")).grid(row=5, column=6)
btn31 = tkinter.Button(root, font=("Arial", 11, "bold"), text="log10", width=7, height=2, bd=5, bg="green",
                     command=lambda: btn_press("log10(")).grid(row=5, column=7)
btn32 = tkinter.Button(root, font=("Arial", 11, "bold"), text="nCr", width=7, height=2, bd=5, bg="green",
                     command=lambda: btn_press("c")).grid(row=5, column=8)
btn33 = tkinter.Button(root, font=("Arial", 11, "bold"), text="sinh", width=7, height=2, bd=5, bg="green",
                     command=lambda: btn_press("sinh(")).grid(row=6, column=5)
btn34 = tkinter.Button(root, font=("Arial", 11, "bold"), text="cosh", width=7, height=2, bd=5, bg="green",
                     command=lambda:btn_press("cosh(")).grid(row=6, column=6)
btn35 = tkinter.Button(root, font=("Arial", 11, "bold"), text="tanh", width=7, height=2, bd=5, bg="green",
                     command=lambda: btn_press("tanh(")).grid(row=6, column=7)
btn36 = tkinter.Button(root, font=("Arial", 11, "bold"), text="nPr", width=7, height=2, bd=5, bg="green",
                     command=lambda: btn_press("p")).grid(row=6, column=8)
btn37 = tkinter.Button(root, font=("Arial", 11, "bold"), text="Ans", width=7, height=2, bd=5, bg="green",
                     command=lambda:equal()).grid(row=7, column=5)
btn38 = tkinter.Button(root, font=("Arial", 11, "bold"), text="x^y", width=7, height=2, bd=5, bg="green",
                     command=lambda:btn_press('**')).grid(row=7, column=6)
btn39 = tkinter.Button(root, font=("Arial", 11, "bold"), text="n!", width=7, height=2, bd=5, bg="green",
                     command=lambda: btn_press(math.factorial(int(text.get())))).grid(row=7, column=7)
btn40 = tkinter.Button(root, font=("Arial", 11, "bold"), text="fix", width=7, height=2, bd=5, bg="green",
                     command=lambda: fix()).grid(row=7, column=8)




#*******************************************************MENU*****************************************************#

def iExit():
	iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
	if iExit>0:
		root.destroy()
		return

def scientific():
	root.resizable(width=False, height=False)
	root.geometry("600x305+0+0")

def standard():
	root.resizable(width=False, height=False)
	root.geometry("285x305+0+0")


menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="standard", command=standard)
filemenu.add_command(label="scientific", command=scientific)
filemenu.add_separator()
filemenu.add_command(label="exit", command=iExit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="copy")
editmenu.add_separator()
editmenu.add_command(label="paste")


helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View Help")




root.config(menu=menubar)
root.mainloop()

















