from random import choice
from time import sleep
lista=[1, 2, 3]
print('=-'*20)
print('''\33[34mFAÇA SUA ESCOLHA!!!\33[m
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
print('=-'*20)
jogo = int(input('Coloque sua escolha:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

print('=-'*20)

pc = choice(lista)

if pc == 1:
    print('O pc escolheu PEDRA')
    if jogo == 1:
        print('Você escolheu PEDRA')
        print('\33[34mEmpatamos! Vamos denovo! ')
    elif jogo == 2:
        print('Você escolheu PAPEL')
        print('\33[31mARGH... Você me venceu. \33[32mPARABÉNS!')
    elif jogo == 3:
        print('Você escolheu TESOURA')
        print('HAHAHA! GANHEI DE VOCÊ!!')
    else:
        print('Você colocou uma opção INVÁLIDA. TENTE NOVAMENTE')
elif pc == 2:
    print('O pc escolheu PAPEL')
    if jogo == 1:
        print('Você escolheu PEDRA')
        print('HAHAHA! GANHEI DE VOCÊ!!')
    elif jogo == 2:
        print('Você escolheu PAPEL')
        print('\33[34mEmpatamos! Vamos denovo! ')
    elif jogo == 3:
        print('Você escolheu TESOURA')
        print('\33[31mARGH... Você me venceu. \33[32mPARABÉNS!')
    else:
        print('Você colocou uma opção INVÁLIDA. TENTE NOVAMENTE')
elif pc == 3:
    print('O pc escolheu TESOURA')
    if jogo == 1:
        print('Você escolheu PEDRA')
        print('\33[31mARGH... Você me venceu. \33[32mPARABÉNS!')
    elif jogo == 2:
        print('Você escolheu PAPEL')
        print('HAHAHA! GANHEI DE VOCÊ!!')
    elif jogo == 3:
        print('Você escolheu TESOURA')
        print('\33[34mEmpatamos! Vamos denovo! ')
    else:
        print('Você colocou uma opção INVÁLIDA. TENTE NOVAMENTE')
