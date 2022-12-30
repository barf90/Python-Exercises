#definindo os produtos e preços na tupla
lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20)
print('--' * 15)
print(' ' * 5, 'LISTA DE PREÇO', ' ' * 5)
print('--' * 15)
#TABULANDO OS PREÇOS E PRODUTOS

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')