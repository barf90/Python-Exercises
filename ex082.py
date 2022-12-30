#python 3 //
#Criando as listas

lista = []
par = []
impar = []

#Colocando os valores na lista principal e pegando resposta se o usuário vai continuar

while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break

#Separando os valores da lista em par e ímpar

for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa é {lista}')
print(f'Os números pares adicionados foram {par}')
print(f'Os números ímpares adicionador foram{impar}')
