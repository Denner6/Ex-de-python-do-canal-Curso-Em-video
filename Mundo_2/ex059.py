from time import sleep
valores = []
for i in range(1, 3):
    valor = int(input(f'Digite o {i}º valor: '))
    valores.append(valor)

opcao = 0
while opcao != 5:

    print('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair
''')
    opcao = int(input('Sua opção: ').strip())

    if opcao == 1:
        # AI aqui soma vai somar os dois valores
        soma = valores[0] + valores[1]
        print(f'A soma dos valores {valores[0]} e {valores[1]} é {soma}')
        print('-='*20)
        sleep(2)

    elif opcao == 2:
        multiplicar = valores[0] * valores[1]
        print(
            f'O resultado de {valores[0]} x {valores[1]}  é {multiplicar}')
        print('-='*20)
        sleep(2)

    elif opcao == 3:
        maior = max(valores)
        print(f'O maior número é {maior}')
        print('-='*20)
        sleep(2)

    elif opcao == 4:
        valores = []
        print('Insira os valores novamente.')
        sleep(1)
        for j in range(1, 3):
            valor = int(input(f'Digite o {j} valor: '))
            valores.append(valor)

    # if valores[0] == valores[1]:
       # print(f'Os números {valores[0]} e {valores[1]} são iguais')
        # print('-='*20)
        # sleep(1.5)
    elif 0 > opcao > 5:
        print('Opção inválida, tente novamente.')
        sleep(1)
print('Finalizando programa...')
sleep(3)
print('Fim do programa, volte sempre')


# OUTRO MODO:

#from time import sleep
#valores = []
# for i in range(1, 3):
#  valor = int(input(f'Digite o {i}º valor: '))
#   valores.append(valor)


# while True:

#  print('''
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair
# ''')
#opcao = int(input('Sua opção: ').strip())

# if opcao == 1:
# AI aqui soma vai somar os dois valores
#soma = valores[0] + valores[1]
#print(f'A soma dos valores {valores[0]} e {valores[1]} é {soma}')
# print('-='*20)
# sleep(2)

# elif opcao == 2:
# multiplicar = valores[0] * valores[1]
# print(
# f'O resultado de {valores[0]} x {valores[1]}  é {multiplicar}')
# print('-='*20)
# sleep(2)

# elif opcao == 3:
# maior = max(valores)
# print(f'O maior número é {maior}')
# print('-='*20)
# sleep(2)

# elif opcao == 4:
#valores = []
#print('Insira os valores novamente.')
# sleep(1)
# for j in range(1, 3):
#   valor = int(input(f'Digite o {j} valor: '))
#    valores.append(valor)#

# if valores[0] == valores[1]:
# print(f'Os números {valores[0]} e {valores[1]} são iguais')
# print('-='*20)
# sleep(1.5)

#    elif opcao == 5:
#        print('Saindo...')
#        sleep(2)
#        print("Fim do programa, volte sempre!")
#        break
#    else:
#        print('Opção inválida, tente novamente.')
#        sleep(1)
