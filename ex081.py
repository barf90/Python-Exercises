#Definindo a lista
numeros = []

#Pegando os números desejados pelo usuário

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break

#Quantidade de números colocados pelo usuário

print(f'A quantidade de numeros digitados foram {len(numeros)}')
numeros.sort(reverse=True)

#Colocando os números em ordem decrescente

print(f'Os numeros ordenados de forma decrescente é {numeros}')

#Checando se o número 5 foi colocado pelo usuário

if 5 in numeros:
    print('O número 5 foi digitado e está na lista.')
else:
    print('O número 5 não foi digitado e não está na lista')
