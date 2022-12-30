n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

#Calculando a média
m = (n1 + n2) / 2

if m < 5.0:
    print('A média desse aluno foi {}, por isso foi \33[31mREPROVADO\33[m'.format(m))
elif m >= 7.0:
    print('A média do aluno foi {}, por isso foi \33[33mAPROVADO\33[m'.format(m))
elif 5.0 <= m < 7:
    print('A média desse aluno foi {}, por isso está de \33[35mRECUPERAÇÃO\33[m'.format(m))
