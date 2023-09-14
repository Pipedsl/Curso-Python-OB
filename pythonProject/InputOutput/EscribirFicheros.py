f = open('mifichero.txt','w') #borra y lo escribe
f.write("datos\n")
f.write("datos2\n")
f.close()

f = open('mifichero.txt','a') #Escribe al final de la linea
f.write("datos\n")
f.write("datos2\n")
f.close()

f = open('mifichero.txt','w') #borra y lo escribe
lista =  [
    'una linea \n',
    'dos lineas\n',
    'tres lineas\n'
]
f.writelines(lista)
f.close()

def escribe(fichero, datos): #funcion para que escriba un fichero , el contenido de la lista
    f = open(fichero,'w')

    for linea in datos:
        if not linea.endswith('\n'): #si la linea no termina en \n se lo agrega al final
            linea = linea + '\n'
        f.write(linea)

    f.close()

lista = [
    'una linea ',
    'dos lineas',
    'tres lineas'
]

escribe('mifichero.txt',lista)