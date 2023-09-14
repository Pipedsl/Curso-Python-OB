class Vehiculo():
    color = ""
    ruedas = 0
    puertas = 0
    print(f"color = {color}, cantidad de ruedas = {ruedas}, cantidad de puertas = {puertas}")

class Coche(Vehiculo):
    def velocidad(self):
        velocidad = 100
        print(f"El Coche tiene una velocidad max de {velocidad}km/h")

    def cilindrada(self):
        cilindrada = 150
        print(f"El Coche tiene {cilindrada}cc")

        

c = Coche()
c.color = "rojo"
c.ruedas = 4
c.puertas = 5
c.velocidad()
c.cilindrada()

print(c)
