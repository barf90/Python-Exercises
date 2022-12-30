s = cont = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foi colocado {cont} números e a soma entre eles é {s}')
