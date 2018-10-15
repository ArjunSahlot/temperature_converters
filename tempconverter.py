from tkinter import *

def displayError(title, mesg):
    q=Tk()
    q.title(title)
    label=Label(q, text = mesg, fg="red", font=("courier new", 16))
    label.grid(row=0, column=1, padx=5, pady=5)
    button=Button(q, text = "OK", width=28, command=q.destroy)
    button.grid(row=3, column=1, padx=15, pady=5,)
    
def convert_fahr():
    words = fbtext.get()
    if words:
        try:
            ftemp = float(words)
        except ValueError as e:
            displayError("Invalid Input", "ERROR: Enter Only Numbers.")        
            return
    else:
        ftemp = 0
    celbox.delete(0, END)
    celbox.insert(0, '%.2f' % (tocel(ftemp)))
    kelbox.delete(0,END)
    kelbox.insert(0, '%.2f' % (tokel(tocel(ftemp))))
    return


def convert_cel():
    words = cbtext.get()
    if words:
        try:
            ctemp = float(words)
        except ValueError as e:
            displayError("Invalid Input", "Enter Only Numbers.")
            return
    else:
        ctemp = 0
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % (tofahr(ctemp)))
    kelbox.delete(0,END)
    kelbox.insert(0, '%.2f' % (tokel(ctemp)))


def convert_kel():
    words = kbtext.get()
    if words:
        try:
            keltemp = float(words)
        except ValueError as e:
            displayError("Invalid Input", "Enter Only Numbers.")
            return
    else:
        keltemp = 0
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % (tofahr(ktoc(keltemp))))
    celbox.delete(0,END)
    celbox.insert(0, '%.2f' % (ktoc(keltemp)))


def tocel(fahr):
    return (fahr-32) * 5.0/9.0


def tofahr(cel):
    return cel * 1.8 + 32


def ktoc(kel):
    return kel - 273.15


def tokel(cel):
    return cel + 273.15


w=Tk()

w.title("My temperature converter")

fahrlabel = Label(w, text='Fahrenheit')
fahrlabel.grid(row=0, column = 0, padx =5, pady=5, sticky = E)

cellabel = Label(w, text='Celsius')
cellabel.grid(row=1, column = 0, padx =5, pady=5, sticky = E)

kellabel = Label(w, text='Kelvin')
kellabel.grid(row=2, column = 0, padx =5, pady=5, sticky = E)

fbtext = StringVar()
fbtext.set('')
fahrbox = Entry(w,textvariable = fbtext)
fahrbox.grid(row=0, column =1, padx=5, pady=5)

cbtext = StringVar()
cbtext.set('')
celbox = Entry(w,textvariable = cbtext)
celbox.grid(row=1, column =1, padx=5, pady=5)

kbtext = StringVar()
kbtext.set('')
kelbox = Entry(w,textvariable = kbtext)
kelbox.grid(row=2, column =1, padx=5, pady=5)

exitbutton = Button(w, text = 'Exit', command = quit)
exitbutton.grid(row = 3, column = 0, padx = 5, pady =5, sticky = N+S+E+W, columnspan=3)

fgobutton = Button(w, text = 'Go', command = convert_fahr)
fgobutton.grid(row = 0, column = 2, padx = 5, pady = 5, sticky=N+S+E+W)

celgobutton = Button(w, text = 'Go', command = convert_cel)
celgobutton.grid(row = 1, column = 2, padx = 5, pady = 5, sticky=N+S+E+W)

kelgobutton = Button(w, text = 'Go', command = convert_kel)
kelgobutton.grid(row = 2, column = 2, padx = 5, pady = 5, sticky=N+S+E+W)


w.mainloop()