#Pedindo o salário atual da pessoa
salario = float(input('Qual seu salário atual? '))

#Calculo do aumento do salário
if salario <= 1250:
    a1 = salario * 0.15 + salario
    print('Com um aumento de 15% do seu salário atual, seu novo salário será de {:.2f}'.format(a1))
else:
    a2 = salario * 0.10 + salario
    print('Com um aumento de 10% do seu salário atual, seu novo salário será de {:.2f}'.format(a2))
