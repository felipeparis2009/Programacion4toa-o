a = int(input("Cual es la temperatura? "))
if a < 10:
    print("Nivel azul")
else:
    if a > 30:
        print("Nivel Rojo")
    else:
        print("Nivel Verde")
