from persona import Persona

def main():
    Fabio = Persona("Fabio", 18)
    Iriem = Persona("Iriem", 20)
    Fabio.imprimir()
    Fabio.cumpleanos()
    print("\n\n\n")
    Iriem.imprimir()
    Iriem.cumpleanos()


if __name__ == "__main__":
    main()