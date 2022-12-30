#Python 3 /// Exercício 94 Curso em vídeo - Mundo 3

#dict dados vai adicionando os dados das pessoas
#list lista local onde os dados vão ser armazenados

dados = {}
lista = []
soma = média = 0

while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas, M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
    print(f'Cadastre a nova pessoa!')
print('-=' * 30)
print(f'Finalizando o cadastramento!')

#quantidade de pessoas cadastradas

print(f'Foram cadastradas {len(lista)} pessoa(as).')

#obtendo a média de idades cadastradas

média = soma / len(lista)
print(f'A média de idade é de {média:5.2f} anos.')

#obtendo lista das mulheres
print('As mulherres cadastradas foram ', end='')
for d in lista:
    if d['sexo'] in 'Ff':
        print(f'{d["nome"]} ', end='')
print()
#obtendo lista de pessoas com idade acima da média
print(f'As pessoas que estão acima da idade média são: ', end='')
for d in lista:
    if d['idade'] > média:
        print(f'{d["nome"]} ', end='')
