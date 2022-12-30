total = cont1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: R$'))
    cont += 1
    total += valor
    if valor > 1000:
        cont1000 += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'O valor total da compra foi de R${total:.2f}')
print(f'O número de produtos com valor maior de R$1000.00 foi de {cont1000}')
print(f'O preço do produto mais barato foi {barato} que custa R${menor:.2f}')
