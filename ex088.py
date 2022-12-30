#definindo a lista das jogadas
from random import randint
from time import sleep

mega = list()
jogos = list()
tot = 1

print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print('-' * 30)

#colocando a quantidade de jogos que o usuário quer
njogos = int(input('Quantos jogos quer que eu sorteie? '))

#Sorteando cada jogo
while tot <= njogos:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
            if cont == 6:
                break
    jogos.sort()
    mega.append(jogos[:])
    jogos.clear()
    tot += 1

#Resultado dos sorteios dos jogos
print('-='*15)
for c in range(0, njogos):
    print(f'Jogo {c + 1}: {mega[c]}')
    sleep(1)
print('-=-=-=-=-=-=-> BOA SORTE <-=-=-=-=-=-=-')
