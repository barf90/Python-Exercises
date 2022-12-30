from datetime import date
cont = 0
contmenor = 0
atual = date.today().year
for a in range(1,8):
    a = int(input('Qual o ano da {}a pessoa: '.format(a)))
    idade = atual - a
    if idade >= 21:
        cont += 1
    else:
        contmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(cont))
print('Ao todo tivemos {} pessoas menores de idade.'.format(contmenor))
