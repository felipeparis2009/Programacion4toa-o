seleccion = str(input("Bienvendio a pizeria bella napoli, ¿quiere una piza vegetariana? si/no"))
if seleccion == "si":
    ingrediente =str(input("selecciono vegetarianao, elija su ingrediente; tofu o pimiento "))
    if ingrediente == "pimiento":
        print("usted eligio vegetariano con pimiento")
    else:
        print("usted eligio vegetariano con tofu")
else:
    ingrediente = str(input("selecciono no vegetariano elija su ingrediente peperoni, jamon o salmon"))
    if ingrediente == "peperoni":
        print(f"usted eligio no vegetariano con {ingrediente}")
    elif ingrediente == "jamon":
        print(f"usted eligio no vegetariano con {ingrediente}")
    else:
        print(f"usted eligio no vegetarianio con {ingrediente}")