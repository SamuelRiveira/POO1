class animal:
    patas = 4
    
    def caminar():
        print("Caminando")

def main():
    vaca = animal
    vaca.caminar()

if __name__ == "__main__":
    main()