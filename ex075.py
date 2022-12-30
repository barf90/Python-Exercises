# pegando os valores do usuário

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))

# colocando os valores em tupla

valores = (a, b, c, d)

print(f'Você digitou os valores {valores}')

# contando a quantidade de 9 na tupla

if 9 in valores:
    print(f'O valor 9 apareceu {valores.count(9)} vezes')
else:
    print('O valor 9 apareceu 0 vezes')

# Achando a posição do número 3

if 3 in valores:
    print(f'O valor 3 está na posição {valores.index(3) + 1}')
else:
    print(f'O valor 3 não foi digitado')

# listando os valores pares
print('Os valores pares digitados foram ', end='')
for n in valores:
    if n%2 == 0:
        print(n, end=' ')