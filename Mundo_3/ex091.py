from operator import itemgetter
from random import randint
from time import sleep
count = 0
jogadores = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)
            }
print('Valores sorteados: ')
for jogador, numero in jogadores.items():
    print(f'    O {jogador} tirou {numero} rolando o dado')
    sleep(1)
print('-='*30)
print('Ranking dos jogadores:')
ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
