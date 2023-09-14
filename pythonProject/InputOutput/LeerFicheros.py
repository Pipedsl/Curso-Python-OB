#permisos:

# r: lectura significa que solo lo voy a leer
# a: append significa que escribire en el fichero pero al final del mismo
# w: escritura voy a borrar y escribir desde cero en el
# x: create voy a crear un fichero si este no existe (es auto en python)


# t: texto
# b: binary


#+

f = open('/etc/passwd','r') #en windows este fichero no existe
datos = f.read()
f.close()

print(datos)

# para windows: https://programminghistorian.org/es/lecciones/trabajar-con-archivos-de-texto
f = open('/etc/passwd','r')
datos = f.readline() #lee la primera linea
f.close()

print(datos)

#si quiero que me lea un fichero linea por lines:
f = open('/etc/passwd','r')
datos = None
while len(datos)>0:
    datos = f.readline()
    print(datos)

f.close()