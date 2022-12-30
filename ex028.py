from random import randint
num = int(input('Tente adivinhar o número que o pc está pensando entre 0 e 10: '))
sort = randint(0,10)
cont = 0
while num != sort:
    cont += 1
    if num < sort:
        num = int(input('[MAIS] Você errou! Tente novamente: '))
    else:
        num = int(input('[MENOS] Você errou! Tente novamente: '))
print('Parabéns você \033[34mACERTOU\033[m, utilizando {} tentativas.'.format(cont + 1))
print('O número sorteado foi {}'.format(sort))

