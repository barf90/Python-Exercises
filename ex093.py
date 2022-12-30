# Python 3 /// Exercício 93 Curso em video - Mundo 3

#Definindo os dados do jogador em um dicionário

dados = {}
partidas = []

dados['Nome'] = str(input('Nome: '))

#npart = número de partidas

npart = int(input('Partidas jogadas: '))

for c in range(0, npart):
    partidas.append(int(input(f'Quantos gols na partida {c + 1}: ')))
dados['gols'] = partidas
dados['total'] = sum(partidas)

print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {dados["Nome"]} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')