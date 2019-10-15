from tkinter import *

listDat = []
def clacProcess(key, strData):
    if key == '=':
        try:
            strData.set(eval(strData.get()))
        except:
            strData.set('Input Error!')
        #print(strData.get())
        finally:
            listDat.clear()
    #TODO
    elif key == 'C':
        listDat.clear()
        strData.set('')

    #efface toutes les touches bufferisées
    elif key == 'AC':
        listDat.clear()
        strData.set('')

    else:
        listDat.append(key)
        strData.set(''.join(listDat))


def cal():
    #main window
    root = Tk()
    root.title("calculatrice")
    root.resizable(0,0)

    #menu
    menuBar = Menu(root, tearoff=0)
    root.config(menu=menuBar)
    filemenu = Menu(menuBar)
    menuBar.add_cascade(label='Mode', menu=filemenu)
    filemenu.add_command(label='Standard', accelerator='Ctrl+S')
    filemenu.add_command(label='Scientific', accelerator='Ctrl+C')
    filemenu.add_separator()
    filemenu.add_cascade(label='?', menu=filemenu)
    filemenu.add_separator()
    menuBar.add_cascade(label='Exit', menu=filemenu)

    strData = StringVar()

    entry=Entry(root,justify=RIGHT,font=('Arial',14),textvariable=strData)
    entry.pack(fill=X)

    #BUTTON
    for buttonKey in ['789/', '456*', '123+', '-0.=', 'CAC()']:

        keyFrame = Frame(root)
        keyFrame.pack()

        for rowKey in buttonKey:
            if len(buttonKey) == 1:

                button=Button(keyFrame,text=rowKey,command=lambda key=rowKey, ent=entry: clacProcess(key, strData), width=32)
                button.pack(side=LEFT)
            else:
                button = Button(keyFrame, text=rowKey,command=lambda key=rowKey, ent=entry: clacProcess(key, strData),  width=5)
                button.pack(side=LEFT)

    root.mainloop()

cal()