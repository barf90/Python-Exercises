n = int(input('Digite um valor inteiro: '))
cont = 1
total = n
media = total / cont
#sn é a variável pra saber a resposta se o usuário quer continuar ou não
sn = ' '
maior = menor = 0
while sn in 'Ss':
    sn = int(input('Quer adicionar mais valores? [S/N]: ')).upper().strip()[0]
    if sn == 'S':
        n = int(input('Digite um valor inteiro: '))
        cont += 1
        total += n
        if total == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
print('Voce colocou {} valores e a média entre eles é {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
