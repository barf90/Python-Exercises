nume = int(input('Coloque um numero de 0 a 9999: '))
u = nume // 1 % 10
d = nume // 10 % 10
c = nume // 100 % 10
m = nume // 1000 % 10
print('Analisando o {}.'.format(nume))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))