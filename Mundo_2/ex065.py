from time import sleep
from timeit import repeat
import colorama
colorama.init()
digitados = []
i = 0
total = 0
while True:

    n = int(input('Digite um número: '))
    digitados.append(n)
    opcao = str(input('Deseja continuar? [S/N] '))
    numbers_typed = len(digitados)
    maior = max(digitados)
    menor = min(digitados)
    if opcao.lower() == 'n':
        print(
            f'Você informou {numbers_typed} números,', end='')
        while i < len(digitados):
            total += digitados[i]/len(digitados)
            i += 1

        break
    elif opcao == ' ':
        print('Opção inválida, Tente novamente.')
        sleep(1)
'''    elif opcao != str:
        print('Por favor, digite um número')
        opcao
        continue'''
print(f'e a  média entre eles é {total}')
print(
    f'O maior número digitado foi \033[32m{maior}\033[m e o menor foi \033[32m{menor}\033[m')
