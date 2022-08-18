import random
from tkinter import *

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def submt(var1):
    if var1.get() == str(resultPLUS()):
        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.3, rely=0.2)
    else:
        wrong = Label(app, text="Wrong!!!", fg="red", font=("Courier", 16))
        wrong.place(relx=0.3, rely=0.2)


def try_again():
    try_again.num1update = random.choice(num)
    try_again.num2update = random.choice(num)
    newQ = Label(
        app, text=f"{try_again.num1update}+{try_again.num2update}", font=("Courier", 16)
    )
    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


def resultPLUS():
    try_again
    return try_again.num1update + try_again.num2update


app = Tk()
app.title("Math For Kids")
# canvas = Canvas(app, width=240, height=300)
# canvas.pack()
app.geometry("600x300")
app.resizable(False, False)
start = Button(app, text="Start", command=try_again)
start.place(relx=0.45, rely=0.2)




solving = Entry(app)
solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)
submit = Button(app, text="Submit", command=lambda: submt(solving))
submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)
try_again = Button(app, text="Try Again", command=try_again)
try_again.place(relx=0.39, rely=0.9)


def open6():
    num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def submt2(var2):
        if var2.get() == str(resultMult()):
            correct = Label(frm, text="Correct!", fg="green", font=("Courier", 16))
            correct.place(relx=0.3, rely=0.2)
        else:
            wrong = Label(frm, text="Wrong!!!", fg="red", font=("Courier", 16))
            wrong.place(relx=0.3, rely=0.2)

    def try_again2():
        try_again2.num1update = random.choice(num2)
        try_again2.num2update = random.choice(num2)
        newQ = Label(
            frm, text=f"{try_again2.num1update}*{try_again2.num2update}", font=("Courier", 16)
        )
        newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

    def resultMult():
        try_again2
        return try_again2.num1update * try_again2.num2update



    frm = Tk()
    frm.grab_set()
    frm.geometry("250x300")
    start2 = Button(frm, text="Start", command=try_again2)
    start2.place(relx=0.45, rely=0.2)
    solving2 = Entry(frm)
    solving2.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)
    submit2 = Button(frm, text="Submit", command=lambda: submt2(solving2))
    submit2.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)
    try_again2 = Button(frm, text="Try Again", command=try_again2)
    try_again2.place(relx=0.39, rely=0.9)
    frm.mainloop()


b1= Button(app, text="*", font=('arial 20 bold'), fg="black", command=open6)
b1.place(relx=0.80, rely=0.4)

def open7():
    num3 = [ 2,  4,  6,  8]

    def submt3(var3):
        if var3.get() == str(resultsub()):
            correct = Label(frm2, text="Correct!", fg="green", font=("Courier", 16))
            correct.place(relx=0.3, rely=0.2)
        else:
            wrong = Label(frm2, text="Wrong!!!", fg="red", font=("Courier", 16))
            wrong.place(relx=0.3, rely=0.2)

    def try_again3():
        try_again3.num1update = random.choice(num3)
        try_again3.num2update = random.choice(num3)
        newQ2 = Label(
            frm2, text=f"{try_again3.num1update} - {try_again3.num2update}", font=("Courier", 16)
        )
        newQ2.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

    def resultsub():
        try_again3
        return try_again3.num1update - try_again3.num2update



    frm2 = Tk()
    frm2.grab_set()
    frm2.geometry("250x300")
    start3 = Button(frm2, text="Start", command=try_again3)
    start3.place(relx=0.45, rely=0.2)
    solving3 = Entry(frm2)
    solving3.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)
    submit3 = Button(frm2, text="Submit", command=lambda: submt3(solving3))
    submit3.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)
    try_again3 = Button(frm2, text="Try Again", command=try_again3)
    try_again3.place(relx=0.39, rely=0.9)
    frm2.mainloop()


b2= Button(app, text="-", font=('arial 20 bold'), fg="black", command=open7)
b2.place(relx=0.20, rely=0.4)

app.mainloop()