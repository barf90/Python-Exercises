from math import sin,cos,tan,radians
ang = float(input('Coloque um ângulo: '))
sen = sin(radians(ang))
co = cos(radians(ang))
ta = tan(radians(ang))
print('O seno de {} é {:.2f}.'.format(ang,sen))
print('O cosseno de {} é {:.2f}.'.format(ang,co))
print('A tangente de {} é {:.2f}.'.format(ang,ta))