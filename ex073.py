# Definindo tupla da ordem dos times

times = ('Palmeiras', 'Atlético-MG', 'Corinthians',
         'Internacional', 'Fluminense', 'Atlético-PR', 'Flamengo',
         'Bragantino', 'São Paulo', 'Ceará SC', 'Santos', 'Botafogo',
         'Avaí', 'Goiás', 'Cuiabá', 'Coritiba', 'América-MG', 'Atlético-GO',
         'Fortaleza', 'Juventude')

# Colocando as informações pedidas (lista dos times, os 5 primeiros colocados,
# os últimos 4 e os times em ordem alfabética.

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os cinco primeiros são {times[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[16:]}')
print('-=' * 15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 15)

print(f'O Botafogo está  {times.index("Botafogo")+1}a posição')