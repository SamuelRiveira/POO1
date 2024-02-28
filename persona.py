class persona:
    def __init__(self, nombre, anos):
        self.nombre = nombre
        self.anos = anos
    def imprimir(self):
        print(f"{self.nombre} tiene {self.anos} años")
    def cumpleanos(self):
        self.anos +=1
        print(f"{self.nombre} ha cumplido {self.anos} años")