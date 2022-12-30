conth = contm20 = cont18 = 0
while True:
    idade = int(input('Coloque a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Coloque o Sexo [F/M]: ')).upper().strip()[0]
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        conth += 1
    if idade < 20 and sexo == 'F':
        contm20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'{cont18} pessoas são maiores de 18')
print(f'{conth} pessoas são homens')
print(f'{contm20} mulheres com menos de 20 anos')
