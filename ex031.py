dist = float(input('Qual a distância da viagem? '))
p1 = dist * 0.50
p2 = dist * 0.45
if dist <= 200:
    print('O preço da passagem pra uma viagem de {}Km será R${}.'.format(dist,p1))
else:
    print('O preço da passagem pra uma viagem de {}Km será de R${}.'.format(dist,p2))
