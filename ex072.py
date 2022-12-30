# python 3 - criando uma tupla
numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze' , 'treze', 'catorze', 'quinze', 'dezesseis',
          'dezessete', 'dezoito', 'dezenove' , 'vinte')

# definindo o número que usuário quer
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0<= n <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numero[n]}')

