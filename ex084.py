#python 3 // código lista de pesos
#definindo a lista de pessoas

lista = list()
dados = list()
pesadas = 0
leves = 0

#Pegando os dados das pessoas

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        pesadas = leves = dados[1]
    else:
        if dados[1] > pesadas:
            pesadas = dados[1]
        if dados[1] < leves:
            leves = dados[1]
    lista.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break

#Número de pessoas que foram cadastradas

print(f'Foram cadastradas {len(lista)} pessoas!')

#Listagem das pessoas mais pesadas e mais leves
print(f'O maior peso foi de {pesadas}Kg. Peso de ', end='')
for p in lista:
    if p[1] == pesadas:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {leves}Kg. Peso de ', end='')
for p in lista:
    if p[1] == leves:
        print(f'{p[0]} ', end='')
print()
