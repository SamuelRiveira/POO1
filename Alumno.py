class alumno:
    def __init__(self):
        self.nota = 0
        self.nombre = ""

    def imprimir(self):
        print(f"La nota del alumno {self.nombre} es {self.nota}")
    
    def promocion(self):
        if self.nota >= 5:
            print(f"El alumno {self.nombre} está promociona")
        else:
            print(f"El alumno {self.nombre} no promociona")