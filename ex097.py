#Python 3 /// Exercício 97 - Mundo 3

def escreva(msg):
    tam = len(msg) + 4
    print(f'~' * tam)
    print(f'  {msg}')
    print(f'~' * tam)


# Código principal
escreva('Olá, Mundo!')
escreva('Vamos dar umas voltas na praia quando formos para lá.')
escreva('Oi!')