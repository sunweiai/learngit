#coding:utf-8

from tkinter import *
from tkinter import filedialog

root = Tk()
root.minsize(300,300)

input_file = StringVar()

#添加文件函数
def inputfile(event):
    print(event)
    #path =
    label_info['text'] = '\n'.join()

def searchpath():
    path = filedialog.askdirectory()
    label_info['text'] = '查找目录:\n'+path


#输入文件名文本框
entry_addfile = Entry(root,font=('arial',12,'bold'),bg = 'skyblue',textvariable = input_file)
entry_addfile.place(x = 10,y = 10,height = 30,width =150)
entry_addfile.bind('<Return>',inputfile)

#选择查找目录
btn_path = Button(root,text = '选择目录',command = searchpath)
btn_path.place(x = 210,y = 10,height = 30,width = 80)

#信息展示
label_info = Label(root,bg = 'powderblue',anchor = 'nw',justify = 'left',font = '隶书')
label_info.place(x = 10,y = 50,height = 240,width = 280)

root.mainloop()