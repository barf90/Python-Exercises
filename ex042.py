l1 = float(input('Coloque o valor do lado 1:'))
l2 = float(input('Coloque o valor do lado 2:'))
l3 = float(input('Coloque o valor do lado 3:'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Com esses seguimentos PODEM FORMAR triângulo.')
    if l1 == l2 == l3:
        print('O triangulo é EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('O triângulo é ESCALENO')
    else:
        print('O triângulo é ISÓSCELES')
else:
    print('Com esses seguimentos NÃO PODE FORMAR triângulo')
