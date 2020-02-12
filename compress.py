#coding:utf-8

from Tkinter import *
import tkFileDialog
import zipfile
import os
import tkMessageBox


root = Tk()
root.minsize(300,400)
root.title('压缩软件1.0')

#定义保存文件路径的变量
paths = ''

#添加文件函数
def addfile():
    global paths
    paths = tkFileDialog.askopenfilenames(title = '选择压缩文件')
    #保存用户选择文件
    filelists = paths.split(' ')
    #print("filelists",filelists)
    #显示用户选取的文件
    label_info['text'] = '\n'.join(filelists)

#压缩函数
def compress():
    #全局化变量
    global filelists
    #创建打开压缩文件
    zp = zipfile.ZipFile('test.zip','a')
    #压缩文件
    for filename in filelists:
        zp.write(filename,os.path.basename(filename))
    #关闭压缩文件
    zp.close()
    #信息提示
    tkMessageBox.showinfo(title = 'messages',message='压缩完成')


#添加按钮
btn_addfile = Button(root,text = '添加文件',command = addfile)
btn_addfile.place(x = 10,y = 20,height =30,width =80)

#压缩按钮
btn_compress = Button(root,text = '压缩文件')
btn_compress.place(x = 110,y = 20,height =30,width =80)

#解压按钮
btn_uncompress = Button(root,text = '解压缩文件')
btn_uncompress.place(x = 210,y = 20,height =30,width =80)

#信息展示区域
label_info = Label(root,bg = 'white',anchor = 'nw',justify = 'left')
label_info.place(x = 10 ,y = 70,width = 280,height = 320)

mainloop()