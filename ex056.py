somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('----{}a PESSOA-----'.format(p))
    nome = str(input('NOME: '.format(p)))
    idade = int(input('IDADE: '.format(p)))
    sexo = str(input('SEXO [M/F]: '.format(p)))
    somaidade += idade
    if p ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = idade / 4
print('A média deste grupo é {} anos'.format(mediaidade))
print('O homem mais velho tem {} ano e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))