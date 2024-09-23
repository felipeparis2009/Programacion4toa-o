a = int (input("cuanta bateria tenes"))
if "a"<20 else:
    print("recargar")
else:
    if a == 20-50:
        print("normal")
    if a == 50-80:
        print("optimo")
    if a >80:
        print("full")