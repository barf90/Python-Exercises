#Python3 /// exercício 91 curso em video Mundo 3

from time import sleep
from random import randint
from operator import itemgetter

jogadores = {}

jogadores['jogador1'] = randint(1,6)
jogadores['jogador2'] = randint(1,6)
jogadores['jogador3'] = randint(1,6)
jogadores['jogador4'] = randint(1,6)

for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)

print('-=' * 20)
print('   ==>RANKING DOS JOGADORES<==   ')

ranking = []

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i + 1} lugar: {v[0]} com {v[1]}.')
    sleep(1)
