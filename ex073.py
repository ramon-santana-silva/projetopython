"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
 na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense."""

clubes=('Palmeiras','Flamengo','Corinthians','Fluminense','Athletico-PR','Internacional','Atlético-MG',
'América-MG','Red Bull Bragantino','Santos','São Paulo','Botafogo','Goiás','Ceará','Fortaleza','Cuiabá',
'Avaí','Coritiba','Atlético-GO','Juventude')

print(f'os 5 primeiros colocados no brasileirão são os clubes: {clubes[0:5]}')
print(f'os ultimos colocados do brasileirão são os clubes:{clubes[16:20]}')
print(f'os clubes do brasileirão em ordem alfabetica {sorted(clubes)}')
print(f'a posição na tabela do América-MG é: {clubes.index("América-MG")+1}')