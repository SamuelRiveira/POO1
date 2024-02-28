"""1º Qué palabra reservada hay que utilizar en lugar de animal (nombre de la clase) para acceder al atributo patas.PendingDeprecationWarning

2º Qué palabra reservada hay que utilizar para crear un nuevo objeto"""

class Animal:
    #patas = 0 #Atributo

    def caminar(self): #Método
        self.patas = 0 #Atributo
        print(f"Caminando con {self.patas} patas")

def main():
    vaca = Animal()
    vaca.patas = 4
    vaca.caminar()

    pato = Animal()
    pato.patas = 2
    pato.caminar()

if __name__ == "__main__":
    main()