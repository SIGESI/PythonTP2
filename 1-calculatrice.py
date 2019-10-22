from tkinter import *
import tkinter.messagebox
import math

listDat = []
root = Tk()

#Méthode permettant d'effectuer les calculs
def clacProcess(key, strData):
    global listDat
    if key == '=':
        try:
            strData.set(eval(strData.get()))
        except:
            strData.set('Input Error!')
        finally:
            listDat.clear()

    elif key == 'C':
        listDat = listDat[: -1]
        strData.set(listDat)

    #efface toutes les touches bufferisées
    elif key == 'AC':
        listDat.clear()
        strData.set('')

    else:
        listDat.append(key)
        strData.set(''.join(listDat))

#Fonction pour le choix menu "exit"
def isExit():
    isExit = tkinter.messagebox.askyesno("Calculatrice","Confirmer si vous voulez quiter.")
    if isExit > 0:
        root.destroy()
        return

#Création de la claculatrice
def calculator():
    #main window
    root.title("calculatrice")
    root.resizable(0,0)

    #menu
    menuBar = Menu(root, tearoff=0)
    root.config(menu=menuBar)
    filemenu = Menu(menuBar)
    menuBar.add_cascade(label="Mode", menu=filemenu)
    filemenu.add_command(label="Standard", accelerator='Ctrl+S')
    filemenu.add_command(label="Scientific", accelerator='Ctrl+C')
    menuBar.add_command(label='Exit', command=lambda: isExit())
    menuBar.add_command(label='?')

    strData = StringVar()

    entry = Entry(root, justify=RIGHT, font=('arial', 20), textvariable=strData, bd=30, insertwidth=4, bg="powder blue").grid(columnspan=4)

    # BUTTON
    bouton7 = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" 7 ", command=lambda: clacProcess("7", strData)).grid(row=1, column=0)
    bouton8 = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" 8 ", command=lambda: clacProcess("8", strData)).grid(row=1, column=1)
    bouton9 = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" 9 ", command=lambda: clacProcess("9", strData)).grid(row=1, column=2)
    boutonDivision = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" / ", command=lambda: clacProcess("/", strData)).grid(row=1, column=3)

    bouton4 = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" 4 ", command=lambda: clacProcess("4", strData)).grid(row=2, column=0)
    bouton5 = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" 5 ", command=lambda: clacProcess("5", strData)).grid(row=2, column=1)
    bouton6 = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" 6 ", command=lambda: clacProcess("6", strData)).grid(row=2, column=2)
    boutonMultiplication = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" * ", command=lambda: clacProcess("*", strData)).grid(row=2, column=3)

    bouton1 = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" 1 ", command=lambda: clacProcess("1", strData)).grid(row=3, column=0)
    bouton2 = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" 2 ", command=lambda: clacProcess("2", strData)).grid(row=3, column=1)
    bouton3 = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" 3 ", command=lambda: clacProcess("3", strData)).grid(row=3, column=2)
    boutonSoustraction = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" - ", command=lambda: clacProcess("-", strData)).grid(row=3, column=3)

    bouton0 = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" 0 ", command=lambda: clacProcess("0", strData)).grid(row=4, column=0)
    boutonParantheseOuvrante = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" ( ", command=lambda: clacProcess("(", strData)).grid(row=4, column=1)
    boutonParantheseFermante = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" ) ", command=lambda: clacProcess(")", strData)).grid(row=4, column=2)
    boutonAddition = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" + ", command=lambda: clacProcess("+", strData)).grid(row=4, column=3)

    boutonPoint = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" . ", command=lambda: clacProcess(".", strData)).grid(row=5, column=0)
    boutonC = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" C ", command=lambda: clacProcess("C", strData)).grid(row=5, column=1)
    boutonAC = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="AC", command=lambda: clacProcess("AC", strData)).grid(row=5, column=2)
    boutonEgal = Button(root, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=" = ", command=lambda: clacProcess("=", strData)).grid(row=5, column=3)

    root.mainloop()

calculator()