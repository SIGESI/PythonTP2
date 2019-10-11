from tkinter import *

listDat = []
# 计算过程
def clacProcess(key, strData):
    # '='则计算结果
    if key == '=':
        try:
            strData.set(eval(strData.get()))  #下一次加入括号
        except:
            strData.set('Input Error!')
        #print(strData.get())
        finally:
            # 原地清除列表
            listDat.clear()

    # efface la dernière touche cliquée  ///pas fini
    elif key == 'C':
        listDat.clear()
        strData.set('')         # 清空显示框

    #efface toutes les touches bufferisées
    elif key == 'A':
        listDat.clear()

        strData.set('')          # 清空显示框

    else:
        listDat.append(key)
        # 列表变量连接成一个字符串
        strData.set(''.join(listDat))


def cal():
    #main window
    root = Tk()    #创建一个主窗口对象
    root.title("calculatrice")
    root.resizable(0,0) #控制移动
    #root.geometry('400x300')   #geometry：窗口大小，大写格式是”宽度x高度+x位置+y位置”【注意不是*是x】，其中x,y将左上角作为（0，0）

    #menu
    menuBar = Menu(root, tearoff=0)
    root.config(menu=menuBar)  #要想显示菜单，必须在“要添加菜单的窗口对象”的config中允许添加上“菜单对象
    filemenu = Menu(menuBar)
    menuBar.add_cascade(label='what? ', menu=filemenu)
    menuBar.add_cascade(label='click me ', menu=filemenu)
    filemenu.add_command(label='aide', accelerator='Ctrl+?') #和上一次的连接？
    filemenu.add_command(label='mode', accelerator='Ctrl+m')

    # 文本框事件绑定
    strData = StringVar()

    #控件对象entry=控件（root【主窗口对象】，参数）
    entry=Entry(root,justify=LEFT,font=('Arial',14),textvariable=strData)
    entry.pack(fill=X)  #强制填充水平方向  fill=X       #grid方法 ：entry.grid(row=0, column=0, columnspan=4, sticky=N+W+S+E, padx=5,  pady=5)

    #BUTTON
    for buttonKey in ['789/', '456*', '123+', '-0.=', 'CA()']:

        keyFrame = Frame(root)   #框架Frame，
        keyFrame.pack()

        for rowKey in buttonKey:
            if len(buttonKey)==1:
                #command:当按下按钮时调用的方法   此处为lambda方法 【强制传入参数】 ///command是控件中的一个参数，如果使得command=函数，那么点击控件的时候将会触发函数（可以用在Button、Menu…）
                button=Button(keyFrame,text=rowKey,command=lambda key=rowKey, ent=entry: clacProcess(key, strData), width=32)
                button.pack(side=LEFT)  #显示
            else:
                button = Button(keyFrame, text=rowKey,command=lambda key=rowKey, ent=entry: clacProcess(key, strData),  width=5)
                button.pack(side=LEFT)

    root.mainloop()      #主窗口持续显示

cal()