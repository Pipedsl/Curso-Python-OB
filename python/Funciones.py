#ALL y ANY : sirven para verificar que todas las funciones de una lista se cumplan o para verificar que alguna de las condiciones de la lista se cumplan

listaA = [1 == 1, 2 == 2, 3 == 4]
res = any(listaA) # con una que se cumpla es suficiente
print(res)

res = all(listaA) #deben cumplirse todas
print(res)

#-----------------------------------------------

#ROUND : redondea

a = 5.5
b = 5.4
c = 5.6
print(round(a))
print(round(b))
print(round(c))

#------------------------------------------------

#MIN : devuelve cual es el minimo de todos los parametros

print(min(1,2,3,4,5,6,7))

#---------------------------------------------------

#POW : para elevar

print(pow(2,4)) # es lo mismo que 2**4

#--------------------------------------------------

#SORTED : sirve para ordenar

lista = ['z','c','d','a']
ordenada = sorted(lista)
print(ordenada)

ordenadaAlreves = sorted(lista, reverse = True)
print(ordenadaAlreves)

ordenadaUsandokey = sorted(lista, reverse = True , key = lambda x : str(x).startswith('a') )
print(ordenadaUsandokey)

#----------------------------------------------------

#INPUT : espera a que el usuario introduzca datos

a = input("como te llamas")

#---------------------------------------------------
#import getpass : Para contraseñas en py, funciona similar al input
