from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''[ 0 ] Pedra
[ 1 ]Papel
[ 2 ]Tesoura''')
jogador = int(input('Qual sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
print('-='*11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*11)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador VENCE!')
    elif jogador ==2:
        print('Computador VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #computador jogou PAPEL
    if jogador ==0:
        print('Computador VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador VENCE!')
    else:
        print('Jogada INVÁLIDA!')

elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('Jogador VENCE!')
    elif jogador == 1:
        print('Computador VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada INVÁLIDA!')
else:
    print('Opção INVÁLIDA!')