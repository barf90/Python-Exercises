#Python 3 /// Exercício 98 - Mundo 3
from time import sleep

def contador(a, b, d):
    if d < 0:
        d *= -1
    if d == 0:
        d = 1
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {d} em {d}')
    sleep(2)

    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += d
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= d
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

# Contador personalizado
print('-=' * 20)
x = int(input('Início:    '))
y = int(input('Fim:       '))
z = int(input('Intervalo: '))
contador(x, y, z)