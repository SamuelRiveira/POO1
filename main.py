"""1º Qué palabra reservada hay que utilizar en lugar de animal (nombre de la clase) para acceder al atributo patas.PendingDeprecationWarning

2º Qué palabra reservada hay que utilizar para crear un nuevo objeto"""

class animal:
    patas = 0
    
    def caminar():
        print(f"Caminando con {animal.patas} patas")

def main():
    vaca = animal
    vaca.patas = 4
    vaca.caminar()

    pato = animal
    vaca.patas = 2
    pato.caminar()

if __name__ == "__main__":
    main()