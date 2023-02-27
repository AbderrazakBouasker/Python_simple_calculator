from tkinter import *
from tkinter import filedialog
from sympy import *
from math import *

temporaryCalculation=""
currentCalculation=""
history = []
symbolsdictionary={"Π":"pi","√":"sqrt","x": "*","²":"**2"}
#variable intiation



def calc():
    window = Tk()
    window.title("Calculator")
    window.geometry("500x540")
    window.config(bg="#EAE0DA")
    window.resizable(False,False)
    #fixed window size color title

    def savescreen():
        global history
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path:
            with open(file_path, 'w') as f:
                for item in history:
                    f.write("%s\n" % item)

    def calculate():
        global currentCalculation, history
        try:
            temporaryCalculation=currentCalculation
            for c in symbolsdictionary:
                temporaryCalculation = temporaryCalculation.replace(c, symbolsdictionary[c])
            # evaluate the expression using sympy
            result = float(sympify(temporaryCalculation))
            # add the expression and result to the history list
            history.append(currentCalculation + " = " + str(result))
            # clear the current calculation and update the history label
            currentCalculation = ""
            historylabel.config(text="\n".join(history))
            resultLabel.config(text="")
        except:
            # handle errors when evaluating the expression
            resultLabel.config(text="Error")
        
    def clear():
        global currentCalculation
        currentCalculation = ""
        resultLabel.config(text=currentCalculation)

    def delete():
        global currentCalculation
        currentCalculation = currentCalculation[:-1]
        resultLabel.config(text=currentCalculation)

    def oper(element):
        global currentCalculation
        currentCalculation+=element
        resultLabel.config(text=currentCalculation)

    #functions declaration
    panel0=Frame(window,borderwidth=1,background="#A0C3D2")
    panel0.pack()
    savebutton=Button(panel0,text="save",height=1,width=1,command=savescreen)
    savebutton.pack(anchor="n")
    #save button position and frame
    panel=Frame(window,borderwidth=2,background="#A0C3D2")
    panel.pack(anchor="center")
    #frame for history
    historylabel=Label(panel,text="\n".join(history),font=("Times New Roman bold",13),width=45,height=8,bg="#EAE0DA")
    historylabel.pack()
    #history label
    panel1=Frame(window,borderwidth=2,background="#A0C3D2")
    panel1.pack(anchor='center',pady=3)
    #added panel set position to top center 
    resultLabel=Label(panel1,height=1,width=35,text=currentCalculation,font=("Times New Roman bold",17),bg="#EAE0DA")
    resultLabel.pack()
    #added label inside frame to show result set font and size
    panel2=Frame(window,background="#A0C3D2",borderwidth=2)
    panel2.pack(anchor="center",side="bottom",pady=5)
    button1=Button(panel2,borderwidth=2,height=2,width=8,text="Del",bg="#b3171f",activebackground="#b3171f", command=clear)
    button1.grid(row=0,column=0,padx=1,pady=1)
    button1.config()
    button2=Button(panel2,borderwidth=2,height=2,width=8,text="AC",command=delete)
    button2.grid(row=0,column=1,padx=1,pady=1)
    button2.config()
    button3=Button(panel2,borderwidth=2,height=2,width=8,text="(")
    button3.grid(row=0,column=2,padx=1,pady=1)
    button3.config(command=lambda:oper("("))
    button4=Button(panel2,borderwidth=2,height=2,width=8,text=")")
    button4.grid(row=0,column=3,padx=1,pady=1)
    button4.config(command=lambda:oper(")"))
    button5=Button(panel2,borderwidth=2,height=2,width=8,text="Π")
    button5.grid(row=0,column=4,padx=1,pady=1)
    button5.config(command=lambda:oper("Π"))

    button11=Button(panel2,borderwidth=2,height=2,width=8,text="7")
    button11.grid(row=1,column=0,padx=1,pady=1)
    button11.config(command=lambda:oper("7"))
    button21=Button(panel2,borderwidth=2,height=2,width=8,text="8")
    button21.grid(row=1,column=1,padx=1,pady=1)
    button21.config(command=lambda:oper("8"))
    button31=Button(panel2,borderwidth=2,height=2,width=8,text="9")
    button31.grid(row=1,column=2,padx=1,pady=1)
    button31.config(command=lambda:oper("9"))
    button41=Button(panel2,borderwidth=2,height=2,width=8,text="÷")
    button41.grid(row=1,column=3,padx=1,pady=1)
    button41.config(command=lambda:oper("/"))
    button51=Button(panel2,borderwidth=2,height=2,width=8,text="√")
    button51.grid(row=1,column=4,padx=1,pady=1)
    button51.config(command=lambda:oper("√("))

    button12=Button(panel2,borderwidth=2,height=2,width=8,text="4")
    button12.grid(row=2,column=0,padx=1,pady=1)
    button12.config(command=lambda:oper("4"))
    button22=Button(panel2,borderwidth=2,height=2,width=8,text="5")
    button22.grid(row=2,column=1,padx=1,pady=1)
    button22.config(command=lambda:oper("5"))
    button32=Button(panel2,borderwidth=2,height=2,width=8,text="6")
    button32.grid(row=2,column=2,padx=1,pady=1)
    button32.config(command=lambda:oper("6"))
    button42=Button(panel2,borderwidth=2,height=2,width=8,text="x")
    button42.grid(row=2,column=3,padx=1,pady=1)
    button42.config(command=lambda:oper("x"))
    button52=Button(panel2,borderwidth=2,height=2,width=8,text="x²")
    button52.grid(row=2,column=4,padx=1,pady=1)
    button52.config(command=lambda:oper("²"))

    button13=Button(panel2,borderwidth=2,height=2,width=8,text="1")
    button13.grid(row=3,column=0,padx=1,pady=1)
    button13.config(command=lambda:oper("1"))
    button23=Button(panel2,borderwidth=2,height=2,width=8,text="2")
    button23.grid(row=3,column=1,padx=1,pady=1)
    button23.config(command=lambda:oper("2"))
    button33=Button(panel2,borderwidth=2,height=2,width=8,text="3")
    button33.grid(row=3,column=2,padx=1,pady=1)
    button33.config(command=lambda:oper("3"))
    button43=Button(panel2,borderwidth=2,height=2,width=8,text="-")
    button43.grid(row=3,column=3,padx=1,pady=1)
    button43.config(command=lambda:oper("-"))
    button53=Button(panel2,borderwidth=2,height=2,width=8,text="x^n")
    button53.grid(row=3,column=4,padx=1,pady=1)
    button53.config(command=lambda:oper("^("))

    button14=Button(panel2,borderwidth=2,height=2,width=8,text="0")
    button14.grid(row=4,column=0,padx=1,pady=1)
    button14.config(command=lambda:oper("0"))
    button24=Button(panel2,borderwidth=2,height=2,width=8,text=".")
    button24.grid(row=4,column=1,padx=1,pady=1)
    button24.config(command=lambda:oper("."))
    button34=Button(panel2,borderwidth=2,height=2,width=8,text="%")
    button34.grid(row=4,column=2,padx=1,pady=1)
    button34.config(command=lambda:oper("%"))
    button44=Button(panel2,borderwidth=2,height=2,width=8,text="+")
    button44.grid(row=4,column=3,padx=1,pady=1)
    button44.config(command=lambda:oper("+"))
    button54=Button(panel2,borderwidth=2,height=2,width=8,text="=",bg="#1f9c19",activebackground="#1f9c19",command=calculate)
    button54.grid(row=4,column=4,padx=1,pady=1)

    window.mainloop()

    




root=Tk()
root.title("Calculator")
root.geometry("500x300")
root.config(bg="#040d57")
root.resizable(False,False)
#fixed window size color title
def launch():
    root.destroy()
    calc()
#function defining
textlabel=Label(root,text="This is a simple calculator \n made using python library Tkinter\n to start testing it press the button below",font=("Times New Roman bold",14),width=45,height=8,bg="#040d57",fg="#ffffff")
textlabel.pack()
#set text color size 
mainbutton=Button(root,text="Open",height=2,width=7,command=launch)
mainbutton.pack()
#button to launch the calculator window

root.mainloop()

