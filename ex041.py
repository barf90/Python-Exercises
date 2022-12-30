from datetime import date
ano = int(input('Coloque seu ano de nascimento: '))

#Contas para ver as idades
atual = date.today().year
idade = atual - ano

print('Você tem {} anos e nasceu no dano de {}.'.format(idade,ano))

if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JÚNIOR')
elif idade <= 25:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')