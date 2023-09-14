import tkinter
from tkinter import ttk

window = tkinter.Tk()

#(0,0)  (1,0)   (2,0)   
#(0,1)  (1,1)   (2,1)   
#(0,2)  (1,2)   (2,2)   
#(0,3)  (1,3)   (2,3)
def reset():
    seleccionado.set(None)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

seleccionado = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='Si', value='1', variable= seleccionado)
r2 = ttk.Radiobutton(window, text='No', value='2', variable= seleccionado)
r3 = ttk.Radiobutton(window, text='Quizas', value='3', variable= seleccionado)

r1.grid(column=0,row=1,pady=5, padx=5)
r2.grid(column=0,row=2,pady=5, padx=5)
r3.grid(column=0,row=3,pady=5, padx=5)

boton = tkinter.Button(window,text='Reset', command=reset)
boton.grid(column=1,row=0)
window.mainloop()