# Python 3 /// Exercício 96 - Mundo 3

def área(larg, comp):
    a = larg * comp
    print(f'A área do Terreno {larg}x{comp} é igual a {a}m².')


# Programa principal
print('     CONTROLE DE TERRENO')
print('-'*30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)