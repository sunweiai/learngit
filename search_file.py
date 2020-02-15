#coding:utf-8

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()
root.minsize(500,300)
root.title('SeachFile soft')

input_file = StringVar()

#添加文件函数
def inputfile(event):

    #获取当前选择的目录路径
    path = label_info['text'].split('\n')[1]
    #获取目录下的文件
    filelists = []
    count = 0

    #获取所有文件列表
    for home,dirs,files in os.walk(path):
        for file in files:
            filelists.append(os.path.join(home,file))

    label_info['text'] += '\n查找到以下文件:'

    #遍历列表所有文件，查找对应文件名的文件
    for filelist in filelists:
        infile = input_file.get()      #获取输入框的文件名
        filename = os.path.basename(filelist)    #获取文件名
        if filename == infile:
            count += 1
            label_info['text'] += '\n'+filelist

    #弹出消息框
    if count == 0:
        label_info['text'] += '\n无'
        messagebox.showinfo(title='消息', message='文件未找到')
    else:
        messagebox.showinfo(title='消息', message='文件已找到')


def searchpath():
    path = filedialog.askdirectory()
    label_info['text'] = '查找目录:\n'+str(path)


#输入文件名文本框
entry_addfile = Entry(root,font=('arial',12,'bold'),bg = 'skyblue',textvariable = input_file)
entry_addfile.place(x = 10,y = 10,height = 30,width =250)
entry_addfile.bind('<Return>',inputfile)

#选择查找目录
btn_path = Button(root,text = '选择目录',command = searchpath)
btn_path.place(x = 310,y = 10,height = 30,width = 80)

#信息展示  ,wraplength设置自动换行
label_info = Label(root,bg = 'powderblue',anchor = 'nw',justify = 'left',font = '隶书',wraplength = 500)
label_info.place(x = 10,y = 50,height = 240,width = 480)

root.mainloop()