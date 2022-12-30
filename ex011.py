h = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
a = h * l
litros = a / 2
print('Você vai precisar de {} litros pra pintar uma parede de {}m²'.format(litros, a))
