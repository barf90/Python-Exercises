#Criando a lista

num = [[], []]
valor = 0

#definindo o lugar que as variáveis vão entrar

for c in range(1,8):
    valor = int(input(f'Digite o {c}o valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

#Ordenando os valores
num[0].sort()
num[1].sort()
#Mostrando os valores pares e ímpares que foram adicionados na lista

print('*-' * 30)
print(f'Os valores pares colocados foram {num[0]}.')
print(f'Os valores ímpares colocados foram {num[1]}')