from time import sleep
primeiros_20_colocados = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí',
                          'Botafogo', 'Ceará SC', 'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense',
                          'Fortaleza', 'Goiás', 'Internacional', 'Juventude', 'Palmeiras', 'Вragantino', 'Santos', 'São Paulo')

print('=-'*20)
print(f'Os vinte primeiros colocados são: {primeiros_20_colocados} ')
sleep(1)
print('=-'*20)
print(f'Os 5 primeiros colocados são: {primeiros_20_colocados[:5]}')
sleep(1)
print('=-'*20)
print(f'Os 4 últimos são: {primeiros_20_colocados[16:]}')
sleep(1)
print('=-'*20)
print(f'Times na ordem alfabética: {sorted(primeiros_20_colocados)} ')
