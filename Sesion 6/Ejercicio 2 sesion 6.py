class Alumno:
    def atributos(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def mostrar(self):
        print(f"Nombre: {self.nombre} \n Nota: {self.nota}")

    def resultado(self):
        if self.nota > 4:
            print("El alumno Aprobo")

        else:
            print("El alumno Reprobo")

alumno1 = Alumno()

alumno1.atributos("Felipe", 3)

alumno1.mostrar()
alumno1.resultado()
              
