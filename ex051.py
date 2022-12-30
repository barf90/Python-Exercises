razao = int(input('Coloque a razão da sua PA: '))
a1 = int(input('Coloque o primeiro termo da sua PA: '))
dec = a1 + (10 - 1) * razao
for c in range(a1, dec + razao , razao):
    print(c, end=' -> ')
print('Acabou!')
