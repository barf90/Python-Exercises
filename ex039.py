import datetime
n1 = int(input('Coloque o ano que você nasceu: '))
#Códigos para ver o ano atual.
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
ano = int(year)    #conversão do ano em str pra int

#Contas para ver as idades
idade = ano - n1
dezo = n1 + 18

if idade == 18:
    print('Como esse ano é o {} e você tem/vai fazer 18 anos, é seu ano de se alistar!!!'.format(dezo))
elif idade < 18:
    faltam = 18 - idade
    print('Como você tem {} anos, faltam {} anos para você se alistar no ano de {}!'.format(idade, faltam, dezo))
else:
    passou = idade - 18
    print('Como você tem {} anos, já passou {} anos que você deveria ter se alistado no ano de {}!'.format(idade, passou, dezo))
