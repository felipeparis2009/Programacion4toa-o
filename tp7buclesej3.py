PIN_SECRETO = "1234"
i = 3
while i < 0:
    INGRESO = str(input("ingreso la contraseña: "))
    if PIN_SECRETO == INGRESO:
        print("bienvendio a su sistema")
    elif i < 0 :
        print("llamando a la policia")
        break
    else:
        i -= 1
        print(f"error, intente nuevamente, restan (i) intentos")