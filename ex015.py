d = float(input('Quantos dias o carro foi alugado: '))
s = float(input('Quantos quilômetros você andou com o carro: '))
#Conta para o valor do aluguel
valor1 = d*60
valor2 = s*0.15
total = valor1 + valor2
print('O valor total do Aluguel é de R${:.2f}.'.format(total))
