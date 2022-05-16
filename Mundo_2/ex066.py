soma = 0
numeros_digitados = []
while True:
    n = int(input(f'Digite um valor (999 para parar): '))
    numeros_digitados.append(n)
    if n == 999:
        break
    soma += n
    maior = max(numeros_digitados)
    menor = min(numeros_digitados)
print(f'A soma dos valores digitados é {soma}')
print(f' o maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
