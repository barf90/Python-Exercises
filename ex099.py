# Python 3 /// Exercício 99 - Mundo 3
from time import sleep

def maior(* valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    print(f'{valores} Foram informados {len(valores)} ao todo.')
    print(f'O maior valor informado foi {max(valores)}.')
    sleep(1)


maior(0,5,6,2)
maior(9,2)
maior(80,5,30,2)
maior(50,2,1)