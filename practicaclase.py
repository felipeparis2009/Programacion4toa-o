want_greet = 's'
valid_options = 0

while want_greet == 's' :
    print('Hola que tal!')
    want_greet = input( '¿Quiere otro saludo?')
    if want_greet not in 'SN' :
        print('No le he entendido pero le saludo igual')
        want_greet = 's'
        break
    valid_options += 1
print(f'{valid_options} respuestas validas')
print('Que tenga un buen dia')
