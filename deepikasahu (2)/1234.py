from tkinter import *
from sqlite3 import *
from tkinter import ttk
import re

root = Tk()
canvasnew = Canvas(root, width=1370, height=700)
canvasnew.place(x=0,y=0)
p1=PhotoImage(file="background2.png")
canvasnew.create_image(0,0,image=p1)
Labelnew=Label(canvasnew,text="Your data has been registered successfully!",fg="brown",bg="white",font=("Georgia",25,"bold"),width=50)
Labelnew.place(x=20,y=100)
but5=Button(canvasnew,text="Back",font=("Georgia",13,"bold"),bg="white",fg="black",padx=40,pady=4).place(x=275,y=230)

