#Pegar os lados do triângulo
print('-='*20)
print('Coloque os lados do triangulo na seguinte ordem:\nMaior seguimento \nLado 1 \nLado 2')
print('-='*20)
ms = float(input('Coloque a medida do Maior seguimento aqui: '))
l1 = float(input('Coloque a medida do lado 1 aqui: '))
l2 = float(input('Cpçpque a medida do lado 2 aqui: '))

#Conta pra saber se é possível ou não formar o triângulo
if l1+l2 > ms:
    print('Com essas medidas esse triângulo é existente!')
else:
    print('Com essas medidas o triângulo não existe!')
