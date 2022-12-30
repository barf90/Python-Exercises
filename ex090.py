#Python3 - exercício 90 curso em vídeo mundo 3
#Definindo a biblioteca
estudante = {}


#pedindo nome e a nota do aluno

estudante['nome'] = str(input('Nome: '))
estudante['nota'] = float(input('Nota: '))

print('-=' * 20)

#definindo a situação dos alunos e colocando a situação dentro do dicionario

if estudante['nota'] >= 7:
    estudante['situacao'] = 'APROVADO'
elif 5 <= estudante['nota'] < 7:
    estudante['situacao'] = 'RECUPERAÇÃO'

else:
    estudante['situacao'] = 'REPROVADO'

#Mostrando o relatório do aluno

for k, v in estudante.items():
    print(f'{k} é igual a {v}')
