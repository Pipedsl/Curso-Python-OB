import tkinter
from tkinter import ttk

window = tkinter.Tk()

#(0,0)  (1,0)   (2,0)   
#(0,1)  (1,1)   (2,1)   
#(0,2)  (1,2)   (2,2)   
#(0,3)  (1,3)   (2,3)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

##Usuario
#Etiqueta usuario
username_label = ttk.Label(window,  text="Username:")
username_label.grid(column=0,row=0, sticky=tkinter.W, padx=5, pady=5)

#Campo usuario
username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

##Pasword
#Etiqueta password
password_label = ttk.Label(window,  text="Password:")
password_label.grid(column=0,row=1, sticky=tkinter.W, padx=5, pady=5)

#Campo password
password_entry = ttk.Entry(window, show='°')
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)


##Boton
login_button = ttk.Button(window, text="Login")
login_button.grid(column=1, row=3, sticky=tkinter.E,  padx=5, pady=5)

window.mainloop()


