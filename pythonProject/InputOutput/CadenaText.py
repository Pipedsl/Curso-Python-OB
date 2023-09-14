cadena= "en un lugar de la manchA"

print(cadena.capitalize()) #mayu solo la primera de la cadena
print(cadena.title()) #mayus cada iniciadora de palabra
print(cadena.count("d")) #contador de letras
print(cadena.lower().count("a")) #se pueden usar mas funciones para realizar algo mas especifico en esta convertir
# todo a minuscula luego cuenta las a

numero = "5"
print(numero.isdigit()) #es propio de las cadenas verifica si la cadena es un numero
print(numero.isalnum()) #es alfa numerico?
print(numero.isalpha()) #es del alfabeto?

cadena= "      en un lugar de la manchA      "
print(cadena)
print(cadena.strip()) #alinea los especioa de la cadena(izquierda o derecha)
print(cadena.lstrip())#quita los espacioes de la izq
print(cadena.rstrip())#quita los espacios de la der

print(cadena.split(" "))#convierte cadena en una lista por el caracter especificado
print(cadena.startswith("en"))# es verdadero si comienza por lo especificado
print(cadena.endswith("mancha"))# true si termina con lo especificado
