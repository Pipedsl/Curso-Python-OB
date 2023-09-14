from functools import reduce
#lista pasada por parametro
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def mifuncion(x):
    if x % 2 !=0:
        return True
    
    return False

#funcion impares con filter
resultado = filter(mifuncion, numeros) 

def suma(a,b):
    return a+b
#suma de todos os elementos con reduce
sumaresult = reduce(suma,list(resultado))

print(sumaresult)