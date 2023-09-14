import tkinter
from tkinter import ttk

window = tkinter.Tk()

#(0,0)  (1,0)   (2,0)   
#(0,1)  (1,1)   (2,1)   
#(0,2)  (1,2)   (2,2)   
#(0,3)  (1,3)   (2,3)

def mifuncion():
    print("seleccionado")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

seleccionado = tkinter.StringVar()
checkbox = ttk.Checkbutton(window, text='acepto las condiciones', variable=seleccionado, command=mifuncion)

checkbox.grid(row=0, column=0)


window.mainloop()