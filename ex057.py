sexo = str(input('Informe seu sexo: [M/F] '))
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))
print('Seu sexo é {}'.format(sexo))
