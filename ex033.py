n1 = int(input('Coloque o primeiro número: '))
n2 = int(input('Coloque o segundo número: '))
n3 = int(input('Coloque o terceino número: '))

if n1 >> n2 & n1 >> n3:
    if n2 >> n3:
        print('O maior número é {} e o menor número é {}'.format(n1,n3))
    else:
        print('O maior número é {} e o menor número é {}.'.format(n1,n2))
elif n2 >> n1 & n2 >> n3:
    if n1 >> n3:
        print('O maior número é {} e o menor número é {}.'.format(n2,n3))
    else:
        print('O maior número é {} e o menor número é {}'.format(n2,n1))
else:
    if n2 >> n1:
        print('O maior número é {} e o menor número é {}.'.format(n3,n1))
    else:
        print('O maior número é o {} e o menor número é {}.'.format(n3,n2))