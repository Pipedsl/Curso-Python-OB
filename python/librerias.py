#FILTER : extrae los resultados o los valores de una lista cuando se cumple el True de la funcion
numeros = [1,2,3,4,5,6,7,8,9,10]

def mifuncion(x):
    if x % 2 ==0:
        return True
    
    return False


resultado = filter(mifuncion, numeros) # se puede hacer con una funcion anonima una lambda
#resultado = filter(lambda x : x %2 ==0, numeros)
print(list(resultado))

#------------------------------------------------------------------------------------------

#MAP : aplica indiscriminadamente la funcion sobre cada elemento de la lista

def cuadrado (x):
    return x * x

resultado = map(cuadrado,[1,2,3,4,5,6,7,8,9])
#resultado = map(lambda x: x * x, [1,2,3,4,5,6,7,8,9]) #como lambda
print(list(resultado))

#--------------------------------------------------------------------------------------------


