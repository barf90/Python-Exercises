numero = int(input('Coloque um número inteiro qualquer para ser convertido: '))
print('Base de conversão: \33[34m1 pra binário; 2 pra octal; 3 pra hexadecimal\33[m.')
base = int(input('Qual base você quer que o número seja convertido? '))

if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Essa não é uma opção válida! Tente novamente.')