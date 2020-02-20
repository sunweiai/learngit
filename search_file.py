#coding:utf-8

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os,sys

root = Tk()
root.minsize(500,300)
root.title('SeachFile soft V1.0')

input_file = StringVar()
input_file.set('input your search file')

#添加文件函数
def inputfile():

    #获取当前选择的目录路径
    path = text_info.get('1.0',END).split('\n')[1]
    if len(path) == 0:
        messagebox.showinfo(title='错误', message='请选择查询目录')
    else:
        searchfile(path)

def searchfile(path):

    #获取目录下的文件
    filelists = []
    count = 0

    #获取所有文件列表
    for home,dirs,files in os.walk(path):
        for file in files:
            filelists.append(os.path.join(home,file))

    text_info.config(state = NORMAL)
    text_info.insert(INSERT,'\n查找到以下文件:')
    #text_info.config(state=DISABLED)

    #遍历列表所有文件，查找对应文件名的文件
    for filelist in filelists:
        infile = input_file.get()      #获取输入框的文件名
        filename = os.path.basename(filelist)    #获取文件名
        if infile in filename:
            count += 1
            text_info.insert(INSERT,'\n'+filelist)

    text_info.config(state=DISABLED)

    #弹出消息框
    if count == 0:
        text_info.config(state = NORMAL)
        text_info.insert(INSERT,'\n无')
        text_info.config(state = DISABLED)
        messagebox.showinfo(title='消息', message='文件未找到')
    else:
        messagebox.showinfo(title='消息', message='文件已找到')

def searchpath():
    global listbox_list
    path = filedialog.askdirectory()
    text_info.config(state = NORMAL)
    text_info.insert(INSERT,"查找目录：\n"+str(path))
    text_info.config(state = DISABLED)

def click(event):
    input_file.set("")


#输入文件名文本框
entry_addfile = Entry(root,font=('arial',12,'bold'),bg = 'skyblue',textvariable = input_file)
entry_addfile.place(relx = 0.02,y = 13)
entry_addfile.bind("<Button-1>",click)

#选择查找目录
btn_path = Button(root,text = '选择目录',command = searchpath)
btn_path.place(relx = 0.5,y = 13 ,height = 30,width = 80)


#查找按钮
btn_search = Button(root,text = '开始',command = inputfile)
btn_search.place(relx = 0.8,y = 13,height = 30,width = 80)

#文本框信息展示
text_info = Text(root,bg = 'powderblue')
text_info.config(state = DISABLED)
text_info.place(relx = 0.02,rely = 0.16,relheight = 0.8,relwidth = 0.95)

#添加滚动条
scroll = Scrollbar(root)
scroll.place(relx = 0.97,rely = 0.16,relheight = 0.8,width = 10)

#文本框与滚动条关联
scroll.config(command = text_info.yview)  #将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
text_info.config(yscrollcommand = scroll.set)  #将滚动条关联到文本框

root.mainloop()