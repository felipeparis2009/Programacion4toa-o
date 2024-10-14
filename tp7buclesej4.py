catetoA = float (input("dame el valor de A"))
catetoB = float (input("dame el valor de b"))

while catetoA <= 0 or catetoB <=0:
    print("error,catetos deben ser mayor que cero")
    catetoA = float(input("dame el valor de A: "))
    catetoB = float(input("dame el valor de b: "))
                 
if catetoA >= 0:
    if catetoB >=0:
        print('(f"el valor de la hipotenusa es: (catetoA**2+catetoB**2)**1/2")')
    else:
        print("B es menor o igual a cero, esto es un error")
else:
    print("A es menor o igual a cero, esto es un error")