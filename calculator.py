#coding:utf-8

from tkinter import *


class Application:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator 1.0")
        self.text_Input = StringVar()
        self.operator = ""
        self.windows()
        self.root.mainloop()

    def windows(self):
        self.txtDisplay=Entry(self.root,font=('arial',20,'bold'),textvariable=self.text_Input,bd=30,
        insertwidth=4,bg="powderblue",justify='right')
        self.txtDisplay.grid(columnspan=4)

        self.btn7=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="7",bg="powderblue",command=lambda:self.btnClick(7))
        self.btn7.grid(row=1,column=0)

        self.btn8=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="8",bg="powderblue",command=lambda:self.btnClick(8))
        self.btn8.grid(row=1,column=1)

        self.btn9=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="9",bg="powderblue",command=lambda:self.btnClick(9))
        self.btn9.grid(row=1,column=2)

        self.Addition=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="+",bg="powderblue",command=lambda:self.btnClick("+"))
        self.Addition.grid(row=1,column=3)
        #================================================================================
        self.btn4=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="4",bg="powderblue",command=lambda:self.btnClick(4))
        self.btn4.grid(row=2,column=0)

        self.btn5=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="5",bg="powderblue",command=lambda:self.btnClick(5))
        self.btn5.grid(row=2,column=1)

        self.btn6=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="6",bg="powderblue",command=lambda:self.btnClick(6))
        self.btn6.grid(row=2,column=2)

        self.Subtraction=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="-",bg="powderblue",command=lambda:self.btnClick("-"))
        self.Subtraction.grid(row=2,column=3)
        #================================================================================
        self.btn1=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="1",bg="powderblue",command=lambda:self.btnClick(1))
        self.btn1.grid(row=3,column=0)

        self.btn2=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="2",bg="powderblue",command=lambda:self.btnClick(2))
        self.btn2.grid(row=3,column=1)

        self.btn3=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="3",bg="powderblue",command=lambda:self.btnClick(3))
        self.btn3.grid(row=3,column=2)

        self.Multiply=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="*",bg="powderblue",command=lambda:self.btnClick("*"))
        self.Multiply.grid(row=3,column=3)
        #================================================================================
        self.btn0=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="0",bg="powderblue",command=lambda:self.btnClick(0))
        self.btn0.grid(row=4,column=0)

        self.btnClear=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="C",bg="powderblue",command=self.btnClearDisplay)
        self.btnClear.grid(row=4,column=1)

        self.btnEquals=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="=",bg="powderblue",command=self.btnEqualsInput)
        self.btnEquals.grid(row=4,column=2)

        self.Division=Button(self.root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="/",bg="powderblue",command=lambda:self.btnClick("/"))
        self.Division.grid(row=4,column=3)

    def btnClick(self,numbers):
        self.operator=self.operator+str(numbers)
        self.text_Input.set(self.operator)

    def btnClearDisplay(self):
        self.operator=""
        self.text_Input.set("")

    def btnEqualsInput(self):
        sumup=str(eval(self.operator))
        self.text_Input.set(sumup)
        self.operator=""

app=Application()