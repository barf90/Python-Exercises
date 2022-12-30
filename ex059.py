from time import sleep
#passo 1: Pegar os dois valores
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opçao = 0
#passo 2: Mostrar as opções do menu
while opçao != 5:

    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')

#passo 3: Escolher a/as opções do menu
    opçao = int(input('Qual das 5 opções você quer escolher? R: '))
#passo 4: Fazer a operação escolhida
    if opçao == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    elif opçao == 2:
        multi = n1 * n2
        print('{} X {} = {}'.format(n1, n2, multi))
    elif opçao == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif opçao == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif opçao == 5:
        print('Programa finalizando...')
    else:
        print('Opção INVÁLIDA! Tente novamente.')
#passo 5: Finalizar
sleep(2)
print('Programa Finalizado!')
