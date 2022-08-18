import tkinter
frm=tkinter.Tk()
from tkinter import ttk
frm.geometry('620x300')
fnt=('None 30 bold')
frm.config(bg='#0B2F3A')
lblnum1=ttk.Label(frm,text='Nimber 1:',font=fnt,background='#DBA901',foreground='black')
lblnum2=ttk.Label(frm,text='Nimber 2:',font=fnt,background='#DBA901',foreground='black')
sv1=tkinter.StringVar()
sv2=tkinter.StringVar()
txtnum1=ttk.Entry(frm,font=fnt,textvariable=sv1)
txtnum2=ttk.Entry(frm,font=fnt,textvariable=sv2)
lblnum1.grid(row=0,column=0)
txtnum1.grid(row=0,column=1)
lblnum2.grid(row=1,column=0)
txtnum2.grid(row=1,column=1)
def calc(ope):
    strn1=str(txtnum1.get())
    strn2=str(txtnum2.get())
    n1=int(strn1)
    n2=int(strn2)
    r=0
    if ope=='+':r=n1+n2
    elif ope=='-':r=n1-n2
    elif ope=='*':r=n1*n2
    else:
        if ope=='/' :r=n1/n2
    lblr['text']=('Result: %s %s %s=%s' % (n1,ope,n2,round(r,2)) )
btns=ttk.Style()
btns.configure('TButton',font=fnt,panding=10)
fram=tkinter.Frame(frm)
btn_width=5
btnadd=ttk.Button(fram,text='+',width=btn_width,style='TButton',command=lambda:calc('+'))
btnsub=ttk.Button(fram,text='-',width=btn_width,style='TButton',command=lambda:calc('-'))
btnmult=ttk.Button(fram,text='*',width=btn_width,style='TButton',command=lambda:calc('*'))
btndiv=ttk.Button(fram,text='/',width=btn_width,style='TButton',command=lambda:calc('/'))
fram.grid(row=2,column=0,columnspan=2)
btnadd.grid(row=0,column=0)
btnsub.grid(row=0,column=1)
btnmult.grid(row=0,column=2)
btndiv.grid(row=0,column=3)
lblr=ttk.Label(fram,text='Result : ',font=fnt)
lblr.grid(row=1,columnspan=4,padx=10)




frm.mainloop()



