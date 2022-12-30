from random import randint
print('-='*14)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*14)
cont = 0
while True:
    pi = int(input('Escolha [1] PAR ou [2] ÍMPAR: '))
    n = int(input('Digite um valor de 1 a 10: '))
    pc = randint(1, 10)
    soma = n + pc
    if pi == 1 and soma % 2 == 0:
        print(f'Eu escolhi {pc} e você {n} somando da {pc + n}')
        print('ARGH VOCÊ GANHOU! VAMOS NOVAMENTE')
    if pi == 2 and soma % 2 != 0:
        print(f'Eu escolhi {pc} e você {n} somando da {pc + n}')
        print('ARGH VOCÊ GANHOU! VAMOS NOVAMENTE')
    if pi == 1 and soma % 2 != 0:
        break
    if pi == 2 and soma % 2 == 0:
        break
    cont += 1
print(f'Você ganhou {cont} vezes seguidas')
print(f'Eu escolhi {pc} e você {n} somando da {pc + n}')
print('EU GANHEI!! HAHAHAHA!')