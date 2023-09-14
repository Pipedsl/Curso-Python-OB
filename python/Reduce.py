#REDUCE : genera un unico resultado sobre una lista, ejecuta ciclicamente la funcion sobre el resultado anterior

from functools import reduce

def suma(a,b):
    print(f'a = {a}, b = {b}')
    return a + b

res = reduce(suma,[1,2,3,4,5])
# res = reduce(lambda a,b: a + b , [1,2,3,4,5]) Funcion anonima LAMBDA
print(res)