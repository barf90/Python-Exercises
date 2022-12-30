#definindo as palavras pra encontrar as vogais

palavras = ('programar', 'aprender', 'astolfo', 'sentir', 'olhar',
            'conter', 'arroz', 'peidar', 'lutar', 'estender')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')