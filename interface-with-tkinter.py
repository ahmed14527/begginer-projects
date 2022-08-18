from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys
supermarket=Tk()
supermarket.geometry('800x450+250+50')
supermarket.resizable(False,False)
supermarket.title("Super Market")
title=Label(supermarket,text='Super Market System',fg='gold',bg='black',font=('tajwal',20))
title.pack(fill=X)
u='https://www.youtube.com/channel/UC0Rh25ARFPvKtfP01sa-dHQ'
#==================================================================================================================
supermarket.config(background='white')
F1=Frame(supermarket,width=460,height=840,bg='#0B2F3A')
F1.place(x=570,y=37)
Title3=Label(F1,text='Contact Us',bg='#0B2F3A',fg='white',font=('tajwal',16,'bold'))
Title3.place(x=40,y=90)
def open():
    webbrowser.open_new(u)
B1 = Button(F1 ,text='Our channel on youtube ', width= 26 , fg= 'black',bg='#DBA901' , font= ('tajwal',11,'bold'),command=open)
B1.place(x=6,y=130)
B5= Button(F1 ,text='لمحه عن المطور  ', width= 26 , fg= 'black' ,bg='#DBA901', font= ('tajwal',11,'bold'))
B5.place(x=6,y=190)

#===================================================================================================================
F2=Frame(supermarket,width=570,height=120,bg='#0B2F3A')
F2.place(x=0,y=330)
photo1=PhotoImage(file="F:\\icons8-supermarket-64.png")
imo1=Label(supermarket,image=photo1)
imo1.place(x=120,y=43,width=308,height=272)
L1=Label(F2,text=" user name ",font=('impact',16),fg='gold',bg='#0B2F3A')
L1.place(x=100,y=20)
L2=Label(F2,text=" password ",font=('tajwal',16),fg='gold',bg='#0B2F3A')
L2.place(x=100,y=65)
En1=Entry(F2,font=('tajwal',12),justify='center')
En1.place(x=200,y=25)
En2=Entry(F2,font=('tajwal',12),justify='center')
En2.place(x=200,y=70)

def log():
    user=En1.get()
    passw=En2.get()
    if user=="admin" and passw=="12345":
        messagebox.showinfo("hello")
        frm = Tk()
        frm.grab_set()
        frm.geometry ('800x450+250+50')

    else:
        messagebox.showinfo("Error")

B=Button(F2, text='log in ', bg='#DBA901', font=('tajwal',12), width=12, height=3, command=log)
B.place(x=400,y=20)
supermarket.mainloop()
