valor = float(input('Qual o valor do produto? R$'))
print('Formas de pagamento: \n [1] cartão; [2] dinheiro;[3] cheque.')
pagamento = int(input('Coloque a forma de pagamento: '))

print('O valor a pagar é: R${}'.format(valor))

if pagamento == 1:
    prestaçoes = int(input('Quantas prestações? '))
    if prestaçoes == 1:
        pagar = valor - valor * 5 / 100
        print('O valor a pagar pelo produto com 5% de desconto é R${}'.format(pagar))
    elif prestaçoes == 2:
        pagar = valor / 2
        print('Cada prestação será de R${}'.format(pagar))
    elif prestaçoes >= 3:
        pagar = (valor + valor * 0.2) / prestaçoes
        print('Sua compra parcelada em {}x a prestação será de R${} com juros.'.format(prestaçoes, pagar))
elif pagamento == 2 and pagamento == 3:
    pagar = valor - valor * 10 / 100
    print('Com 10% de desconto o valor do produto é R${}'.format(pagar))
else:
    pagar = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} será de R${:.2f} no final.'.format(valor, pagar))
