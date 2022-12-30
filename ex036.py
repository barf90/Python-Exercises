casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = float(input('Quantos anos você vai pagar a casa? '))

# Contas para saber as prestações da casa e se é possível financiar a casa.
prestaçoes = casa / (anos * 12)
sal = salario * 0.30

print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}.'.format(casa,anos,prestaçoes))

if prestaçoes >= sal:
    print('O empréstimo foi \33[31mNEGADO\33[m')
else:
    print('O empréstimo pode ser \33[32mCONCEDIDO\33[m')
