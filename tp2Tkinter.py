from tkinter import *

window = Tk()
window.title('My Window')
window.geometry('500x300')  # 这里的乘是小x
l = Label(window, text='Hello！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
l.pack()
window.mainloop()