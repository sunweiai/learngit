#coding:utf-8

from Tkinter import *

root = Tk()

def evaluate(event):
    data = nameinpt.get()
    ans.configure(text="Answer:"+str(eval(data)))

title = Label(text="请输入你的表达式:")
title.pack()

nameinpt = Entry(root)
nameinpt.bind("<Return>",evaluate)
nameinpt.pack()

ans = Label(root)
ans.pack()

root.mainloop()