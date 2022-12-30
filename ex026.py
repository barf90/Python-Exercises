frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('Na sua frase a letra "A" aparece {} vezes.'.format(frase.count('A')))
print('A letra "A" aparece primeiro na posição {}.'.format(frase.find('A')+1))
print('A letra "A" aparece por último na posição {}'.format(frase.rfind('A')))