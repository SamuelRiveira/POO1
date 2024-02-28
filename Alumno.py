class alumno:
    def __init__(self, nombre, nota):
        self.nota = nota
        self.nombre = nombre

    def imprimir(self):
        print(f"La nota del alumno {self.nombre} es {self.nota}")
    
    def promocion(self):
        if self.nota >= 5:
            print(f"El alumno {self.nombre} promociona")
        else:
            print(f"El alumno {self.nombre} no promociona")