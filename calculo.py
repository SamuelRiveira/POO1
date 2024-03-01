class Calculo:
    def __init__(self, numero1:int, numero2:int):
        self.numero1 = numero1
        self.numero2 = numero2

    def suma(self):
        resultado = self.numero1 + self.numero2
        print(f"El resultado de la suma es: {resultado}")
    
    def resta(self):
        resultado = self.numero1 - self.numero2
        print(f"El resultado de la resta es: {resultado}")
    
    def multiplicacion(self):
        resultado = self.numero1 * self.numero2
        print(f"El resultado de la multiplicacion es: {resultado}")
    
    def division(self):
        resultado = self.numero1 / self.numero2
        print(f"El resultado de la division es: {resultado}")
    
if __name__ == "__main__":
    sum = Calculo(2, 7)
    sum.suma()

    rest = Calculo(15, 10)
    rest.resta()

    mult = Calculo(6, 4)
    mult.multiplicacion()

    div = Calculo(60, 2)
    div.division()