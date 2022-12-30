peso = float(input('Coloque seu peso (Kg) : '))
altura = float(input('Coloque sua altura (m):'))

#Cálculo do IMC
IMC = peso / (altura ** 2)

print('Seu peso é {} kg e sua altura é {} metros'.format(peso,altura))
if IMC < 18.5:
    print('Seu IMC é {:.2f}, por isto está abaixo do peso'.format(IMC))
elif 18 <=IMC < 25:
    print('Seu IMC é {:.2f}, por isto está no peso ideal'.format(IMC))
elif 25 <= IMC < 30:
    print('Seu IMC é {:.2f}, por isto está com sobrepeso'.format(IMC))
elif 30 <= IMC < 40:
    print('Seu IMC é {:.2f}, por isto está com obesidade'.format(IMC))
elif IMC >= 40:
    print('Seu IMC é {:.2f}, por isto está com obesidade mórbida'.format(IMC))
