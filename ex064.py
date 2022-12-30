total = n = cont = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    total = total + n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} numeros e a soma deles foi {}'.format(cont,total))
