vel = float(input('Qual a velocidade que o carro passou pelo radar? '))
pag = (vel - 80) * 7
if vel <= 80:
    print('O carro não levou multa, pq passou a {}Km/h'.format(vel))

else:
    print('O carro passou a {}Km/h, a multa sera de R${}.'.format(vel,pag))
