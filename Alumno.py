class alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"La nota del alumno {self.nombre} es {self.nota}")
    
    def promocion(self):
        if self.nota >= 5:
            print(f"El alumno {self.nombre} promociona")
        else:
            print(f"El alumno {self.nombre} no promociona")