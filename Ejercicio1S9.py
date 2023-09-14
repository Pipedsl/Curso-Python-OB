#pedir paises por consola (separados por comas)
paises = input("Ingrese paises separados por coma\n")
#Almacenar paises en una lista
lista = paises.split(",")
#evitar  paises repetidos
listanoRep = list(set(lista))
#mostrar por consola lista ordenada
print(sorted(listanoRep))