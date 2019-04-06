from s37uptime import *
from tkinter import *
def maj():
    temp = s37uptime()
    afficher = 'L\'ordinateur fonctionne depuis :\n{}h{:02d}minutes'.format(temp[0],
    temp[1])
    affichemoi.set(afficher)
    w.after(10000, maj)
def doQuitter(caraboule):
    w.destroy()
w = Tk()
affichemoi = StringVar()
label01=Label(w, textvariable=affichemoi)
label01.pack()
label01.bind(sequence="<Button>", func=doQuitter)
w.title('Uptime')
w.overrideredirect(1)
maj()
w.mainloop()