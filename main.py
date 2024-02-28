from persona import persona

def main():
    Fabio = persona("Fabio", 18)
    Iriem = persona("Iriem", 20)
    Fabio.imprimir()
    Fabio.cumpleanos()
    print("\n\n\n")
    Iriem.imprimir()
    Iriem.cumpleanos()


if __name__ == "__main__":
    main()