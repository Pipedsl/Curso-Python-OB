import tkinter
from tkinter import ttk

window = tkinter.Tk()

def mifuncion():
    print("seleccionado")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

seleccionado = tkinter.StringVar()
checkbox = ttk.Checkbutton(window, text='Me gustan las clases', variable=seleccionado, command=mifuncion)
checkbox.grid(row=0, column=0)
seleccionado2 =  tkinter.StringVar()
checkbox2 = ttk.Checkbutton(window, text='Me encantan las clases', variable=seleccionado2, command=mifuncion)
checkbox2.grid(row=0, column=1)
label = tkinter.Label(window,text='Hola OpenBootcamp',)
label.grid(column=1,row=1, sticky=tkinter.W, padx=5, pady=5)

window.mainloop()