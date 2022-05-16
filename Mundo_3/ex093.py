dados = dict()
lista_de_gols = list()

dados['Nome do jogador'] = input('Nome do jogador: ').title()
partidas_jogadas = int(input(f'Quantas partidas {dados["Nome do jogador"]} jogou? '))

for i in range(0, partidas_jogadas):
    lista_de_gols.append(int(input(f'  Quantos gols na partidas {i+1}? ')))
dados['Gols por partida'] = lista_de_gols[:]
dados['Total de gols'] = sum(lista_de_gols)

print('-='*30)

for key, valor in dados.items():
    print(f'{key} tem o valor \033[32m{valor}\033[m')

print('-='*30)
print(f'O jogador {dados["Nome do jogador"]} jogou {partidas_jogadas} partidas.')

for i, gols in enumerate(dados['Gols por partida']):

    print(f'  → Na partida {i+1}, fez \033[33m{gols}\033[m gols')
print(f'No total {dados["Nome do jogador"]} fez \033[34m{dados["Total de gols"]}\033[m gols')
