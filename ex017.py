from math import hypot
co = float(input('Coloque o valor do cateto oposto: '))
ca = float(input('Coloque o valor do cateto adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa é igual: {}'.format(hi))
