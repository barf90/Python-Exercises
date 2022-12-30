print('-=' * 10)
print('\033[34mGERADOR DE TABUADA\033[m')
print('-=' * 10)
tabuada = cont = 0
while True:
    n = int(input('Quer a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('PROGRAMA ENCERRADO!')
