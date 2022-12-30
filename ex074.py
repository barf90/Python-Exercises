from random import randint

# criar a tupla com os números randomizados
a = randint(1,10)
b = randint(1,10)
c = randint(1,10)
d = randint(1,10)
e = randint(1,10)

numeros = (a, b, c, d, e)
print('Os valores sorteados foram:')
for n in numeros:
    print(f'{n} ', end='')

# achar o menor e maior número

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')