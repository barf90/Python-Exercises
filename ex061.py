'''a1 = int(input('Primeiro termo da sua PA: '))
r = int(input('Coloque a razão da PA: '))
c = a1
pa = 1
while pa <= 10:
    print('{} -> '.format(c), end='')
    c += r
    pa += 1
print(' FIM')'''
a1 = int(input('Primeiro termo da sua PG: '))
q = int(input('Coloque a razão da PG: '))
c = a1
pg = 1
while pg <= 10:
    print('{} -> '.format(c),end='')
    c *= q
    pg += 1
print(' FIM')