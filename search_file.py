#coding:utf-8

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os,sys

class SearchFile:

    def __init__(self):
        self.root = Tk()
        self.root.minsize(500, 300)
        self.root.title('SeachFile soft V1.0')
        self.input_file = StringVar()
        self.input_file.set('input your search file')
        self.windows()
        self.root.mainloop()

    # 添加文件函数
    def inputfile(self):

        # 获取当前选择的目录路径
        path = self.text_info.get('1.0', END).split('\n')[1]
        if len(path) == 0:
            messagebox.showinfo(title='错误', message='请选择查询目录')
        else:
            self.searchfile(path)

    def searchfile(self,path):

        # 获取目录下的文件
        filelists = []
        count = 0

        # 获取所有文件列表
        for home, dirs, files in os.walk(path):
            for file in files:
                filelists.append(os.path.join(home, file))

        self.text_info.config(state=NORMAL)
        self.text_info.insert(INSERT, '\n查找到以下文件:')
        # text_info.config(state=DISABLED)

        # 遍历列表所有文件，查找对应文件名的文件
        for filelist in filelists:
            infile = self.input_file.get()  # 获取输入框的文件名
            filename = os.path.basename(filelist)  # 获取文件名
            if infile in filename:
                count += 1
                self.text_info.insert(INSERT, '\n' + filelist)
        self.text_info.config(state=DISABLED)

        # 弹出消息框
        if count == 0:
            self.text_info.config(state=NORMAL)
            self.text_info.insert(INSERT, '\n无')
            self.text_info.config(state=DISABLED)
            messagebox.showinfo(title='消息', message='文件未找到')
        else:
            messagebox.showinfo(title='消息', message='文件已找到')

    def searchpath(self):
        path = filedialog.askdirectory()
        self.text_info.config(state=NORMAL)
        self.text_info.delete('1.0', END)
        self.text_info.insert(INSERT, "查找目录：\n" + str(path))
        self.text_info.config(state=DISABLED)

    def click(self,event):
        self.input_file.set("")

    def windows(self):
        # 输入文件名文本框
        self.entry_addfile = Entry(self.root, font=('arial', 12, 'bold'), bg='skyblue', textvariable=self.input_file)
        self.entry_addfile.place(relx=0.02, y=13)
        self.entry_addfile.bind("<Button-1>", self.click)

        # 选择查找目录
        self.btn_path = Button(self.root, text='选择目录', command=self.searchpath)
        self.btn_path.place(relx=0.5, y=13, height=30, width=80)

        # 查找按钮
        self.btn_search = Button(self.root, text='开始', command=self.inputfile)
        self.btn_search.place(relx=0.8, y=13, height=30, width=80)

        # 文本框信息展示
        self.text_info = Text(self.root, bg='powderblue')
        self.text_info.config(state=DISABLED)
        self.text_info.place(relx=0.02, rely=0.16, relheight=0.8, relwidth=0.95)

        # 添加滚动条
        self.scroll = Scrollbar(self.root)
        self.scroll.place(relx=0.97, rely=0.16, relheight=0.8, width=10)

        # 文本框与滚动条关联
        self.scroll.config(command=self.text_info.yview)  # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
        self.text_info.config(yscrollcommand=self.scroll.set)  # 将滚动条关联到文本框

searchfile = SearchFile()