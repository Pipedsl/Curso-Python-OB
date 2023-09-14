import pickle # permite serializar y deserializar
class Juguete:
    nombre=""
    precio = 0.0

    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre

#serializar convertir la represetacion de un programa en una secuencia de datos que podemos escribir en un fichero
#j1 = Juguete("Potato", 10.5) #guardado el fichero en datos.bin
#f = open('datos.bin','wb')
#pickle.dump(j1, f)
#f.close()


#deserializar es lo contrarios datos de un fichero a la representacion de un programa
f = open('datos.bin', 'rb')
potato = pickle.load(f)
f.close()

print(type(potato))
print(potato.getNombre(), "precio: ", potato.precio)