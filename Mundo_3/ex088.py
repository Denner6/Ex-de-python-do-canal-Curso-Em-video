from random import randint
from time import sleep

lista = list()
jogos = list()
total_de_jogos = 1

print('-'*60)
print('         Sorteador de números para mega sena')
print('-'*60)

quantidade_de_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print('-='*5, f' SORTEANDO {quantidade_de_jogos} JOGOS', '-='*5)

while total_de_jogos <= quantidade_de_jogos:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total_de_jogos += 1
    
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print('-='*5, '< BOA SORTE! > ', '-='*5)
