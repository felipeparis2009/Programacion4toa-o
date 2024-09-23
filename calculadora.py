def suma (a,b):
    return a+b
def resta(a,b):
    return(a-b)
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def poten(x,y):
    return x**y
def raiz(x,y):
    return (x**(1/y))
# este espacio es para crear la funcion calculadora
x = float(input("dame el valor de a"))
y = float(input("dame el valor de b"))
print("si queres sumar ingresa A")
print("si queres restar ingresa B")
print("si queres multiplicar ingrea C")
print("si queres dividir ingresa D")
print("si queres potenciar ingresa E")
print("si queres la rais de ingresa F")
fun = str(input("selecciona la opcion deseada "))
match fun:
    case "A":
        print(suma (x,y))
    case "B":
        print(resta(x,y))
    case "C":
        print(mult(x,y))
    case "D":
        print(div(x,y))
    case "E":
        print(poten(x,y))
    case "F":
        print(raiz(x,y))
