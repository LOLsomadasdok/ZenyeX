
from re import sub
from tkinter import *
import os
import subprocess
print(os.path)
window = Tk()
window.title("ZenyeX10 V0.0.1")
window.geometry('500x300')
window.configure(background='#808080')

lbl = Label(window,text="SystemXen Tech Team © ",fg="white",bg="#808080",font=("Arial Black",10))

lbl.grid(column=0, row=0)
lbzl = Label(window, text="Cmd:",fg="white",bg="#808080",font=("Arial Black",8))
lbzl.grid(column=1, row=0)

lbl.grid(column=0, row=0)
txt = Entry(window,width=20,fg="white",bg="#000000",font=("Arial Black",8),border=0)

txt.grid(column=2, row=0)


def clicked():
    subprocess.run(str(txt.get()), shell=True)
def dela():
    subprocess.run("powershell .\\dela.ps1", shell=True)
def delx():
    subprocess.run("powershell .\\delx.ps1", shell=True)
def delz():
    subprocess.run("powershell .\\delz.ps1", shell=True)
def rex():
    subprocess.run("rex.cmd", shell=True)
def delm():
    subprocess.run("powershell .\\delm.ps1", shell=True)


btn = Button(window,text="Execute",activeforeground="red", command=clicked,fg="white",bg="#000000",font=("Arial Black",8),border=0,activebackground="black")
btn1 = Button(window, text="Delete Sticky Notes", command=dela,fg="white",bg="#000000",font=("Arial Black",8),border=0,activeforeground="red",activebackground="black")
btn2 = Button(window, text="Delete Calculator", command=delx,fg="white",bg="#000000",font=("Arial Black",8),border=0,activeforeground="red",activebackground="black")
btn3 = Button(window, text="Delete OneNote", command=delz,fg="white",bg="#000000",font=("Arial Black",8),border=0,activeforeground="red",activebackground="black")
btn4 = Button(window, text="Restart Explorer", command=rex,fg="white",bg="#000000",font=("Arial Black",8),border=0,activeforeground="red",activebackground="black")
btn5 = Button(window, text="Delete Microsoft Store", command=delm,fg="white",bg="#000000",font=("Arial Black",8),border=0,activeforeground="red",activebackground="black")
btn.grid(column=3, row=0)
btn1.grid(column=0, row=1)
btn2.grid(column=2, row=1)
btn3.grid(column=3, row=1)
btn4.grid(column=0, row=2)
btn5.grid(column=2, row=2)
window.mainloop()