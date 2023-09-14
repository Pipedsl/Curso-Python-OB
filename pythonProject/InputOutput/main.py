numero = 511
texto = "quijote"
otromas = 1.2

#formateo version vieja:
print("El numero es%d y el texto es %s y tiene %f" %(numero,texto,otromas))
#formateo el flotante para que tenga menos decimales = %.2f (dos decimales)
print("Valor flotante: %.1f" %otromas) #un solo decimal
 # forma muy arcaica ya no utilizada
#-----------------------------------------------------------------------------
#formato habitual hasta python 3.6
print("El numero es {} y el texto es {} y tiene {}"
      .format(texto,numero,otromas) # se puede utilizar en desorden
)
print("El numero es {1} y el texto es {0} y tiene {2}"
      .format(texto,numero,otromas) # ordenar con index en las llaves{}
)
print("El numero es {n1} y el texto es {texto} y tiene {otromas}"
      .format(texto = texto,n1 = numero, otromas = otromas)
)
#----------------------------------------------------------------------------
#La mejor forma de hacerlo hoy en día es:
print(f"El numero es{numero} y el texto es {texto} y tiene {otromas}")
print(f"El numero es{numero} y el texto es {texto.upper()} y tiene {otromas}")