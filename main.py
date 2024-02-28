from persona import Persona

def main():
    fabio = Persona("Fabio", 18)
    iriem = Persona("Iriem", 20)
    fabio.imprimir()
    fabio.cumpleanos()
    print("\n\n\n")
    iriem.imprimir()
    iriem.cumpleanos()


if __name__ == "__main__":
    main()