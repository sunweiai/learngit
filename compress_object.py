#coding:utf-8
from tkinter import *
from tkinter import filedialog
import zipfile
import os
from tkinter import messagebox

class Compress_soft:
    # 定义保存文件路径的变量
    filelists = []

    def __init__(self):
        self.root = Tk()
        self.root.minsize(300, 400)
        self.root.title('压缩软件1.0')
        self.widows()

        mainloop()

    def widows(self):
        # 添加按钮
        self.btn_addfile = Button(self.root, text='添加文件', command=self.addfile)
        self.btn_addfile.place(x=10, y=20, height=30, width=80)

        # 压缩按钮
        self.btn_compress = Button(self.root, text='压缩文件', command=self.compress)
        self.btn_compress.place(x=110, y=20, height=30, width=80)

        # 解压按钮
        self.btn_uncompress = Button(self.root, text='解压缩文件', command=self.uncompress)
        self.btn_uncompress.place(x=210, y=20, height=30, width=80)

        # 信息展示区域
        self.label_info = Label(self.root, bg='white', anchor='nw', justify='left')
        self.label_info.place(x=10, y=70, width=280, height=320)

    # 添加文件函数
    def addfile(self):
        paths = filedialog.askopenfilenames(title='选择压缩文件')
        # 保存用户选择文件
        for path in paths:
            self.filelists.append(path)
        # print("filelists",filelists)
        # 显示用户选取的文件
        self.label_info['text'] = '\n'.join(self.filelists)

    # 压缩函数
    def compress(self):
        # 设置压缩文件路径
        zippath = filedialog.asksaveasfilename(filetype=(('zip文件', '*.zip'),))
        try:
            # 创建打开压缩文件
            zp = zipfile.ZipFile(zippath, 'a')
            # 压缩文件
            for filename in self.filelists:
                zp.write(filename, os.path.basename(filename))
        except Exception as e:
            messagebox.showinfo(title='messages', message='压缩失败')
        else:
            messagebox.showinfo(title='messages', message='压缩完成')
        # 关闭压缩文件
        finally:
            zp.close()
        # 信息提示

    def uncompress(self):
        # 获取压缩文件位置
        zippath = filedialog.askopenfilename()
        try:
            # 打开压缩文件
            zp = zipfile.ZipFile(zippath, 'r')
        except FileNotFoundError as e:
            messagebox.showinfo(title='error', message=e)
        # 解压
        dirpath = filedialog.askdirectory()
        zp.extractall(dirpath)
        # 关闭压缩文件
        zp.close()

comp = Compress_soft()