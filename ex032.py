#ano = int(input('Coloque um ano: '))
#bis = ano%4
#cem = ano%100
#if bis == 0:
#    if cem != 0:
#        print('O ano de {} é bissexto.'.format(ano))
#    else:
#        print('O ano de {} não é bissexto.'.format(ano))
#
#else:
#    print('O ano de {} não é bissexto'.format(ano))

ano = int(input('Coloque um ano: '))
if (ano%4 == 0) & (ano%100 != 0) | (ano%400 == 0):
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))