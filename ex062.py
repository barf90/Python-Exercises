print('GERADOR DE PA')
print('-=' * 10)
a1 = int(input('Primeiro termo da sua PA: '))
r = int(input('Coloque a razão da PA: '))
c = a1
pa = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while pa <= total:
        print('{} -> '.format(c), end='')
        c += r
        pa += 1
    print(' PAUSA')
    mais = int(input('Quantos termos  você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
