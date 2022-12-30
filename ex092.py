#Python 3 /// Exercício 92 Cusro em video - Mundo 3
from datetime import datetime
#Criando dicionário

dados = {}

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['cpts'] = int(input('Número da carteira de trabalho: '))

#Continuação para aqueles que tem carteira de trabalho
print('-=' * 30)
if dados['cpts'] == 0:
    for k, v in dados.items():
        print(f'{k} tem valor igual a {v}')

else:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['contratação'] - nasc + 35
    for k, v in dados.items():
        print(f'    - {k} tem o valor {v}')
    