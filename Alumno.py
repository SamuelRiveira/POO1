class alumno:
    def imprimir(self):
        self.nombre = ""
        self.nota = 0
        print(f"La nota del alumno {self.nombre} es {self.nota}")
    def promocion(self):
        self.nombre = ""
        self.nota = 0
        if self.nota >= 5:
            print(f"El alumno {self.nombre} está promociona")
        else:
            print(f"El alumno {self.nombre} no promociona")