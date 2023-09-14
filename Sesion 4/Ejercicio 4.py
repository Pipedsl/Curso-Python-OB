# funcion que pueda decir si un año es bisiesto o no



def añoBisiesto(año):
    if año%4 == 0:
        print(f"{año} corresponde a un año bisiesto!")
    else:
        print(f"{año} no es un año bisiesto!")

añoBisiesto(int(input("Ingrese el año que desea comprobar\n-->")))

