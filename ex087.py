#definindo a matriz

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
#colocando os valores dentro da matriz

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valora para a posição [{l},{c}]: '))

#montando a matriz
print('-=' * 40)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')

#fazendo os cálculos da matriz
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        if matriz[1][c] == 0:
            mai = matriz[1][c]
        else:
            if matriz[1][c] > mai:
                mai = matriz[1][c]
    print()
for l in range(0,3):
    scol += matriz[l][2]

print(f'A soma dos valores pares é {spar}')
print(f'A soma da 3a coluna é {scol}')
print(f'O maios valor da segunda linha é {mai}')
