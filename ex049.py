num = float(input('Coloque o número que você quer a tabuada: '))
for c in range(1, 11):
    tab = c * num
    print('{} X {} = {}'.format(num, c, tab))
