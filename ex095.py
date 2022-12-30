#Python 3 /// Exercício 95 - Curso em vídeo - Mundo 3

#dicionário de jogadores e lista dos dados
jogador = {}
gols = []
dados = []

#Pegando informações dos jogadores
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome: '))
    npart = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    gols.clear()
    for c in range(0,npart):
        gols.append(int(input(f'Gols na partida {c + 1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    dados.append(jogador.copy())
    
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

#mostra dos resultados
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(dados):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

#Escolhendo o jogador para mostrar os dados.
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(dados):
        print(f'ERRO! Não existe jogador com codigo {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {dados[busca]["Nome"]}:')
        for i, g in enumerate(dados[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')

print('<<<<< PROGRAMA FINALIZADO, VOLTE SEMPRE >>>>>')
