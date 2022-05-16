numeros = []
soma = 0
while True:
    n = int(input('Digite um valor: ').strip())
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
        soma += n
    else:
        print('Valor duplicado! Não irei adicionar...')
    continuar = ''
    while continuar != 's' and continuar != 'n':
        continuar = input('Você deseja continuar? [S/N] ').lower()

    if continuar == 'n':
        break

numeros = sorted(numeros)
print('-='*30)
print(f'Você digitou os valores: {", ".join(map(str,numeros))}')
print(f'A soma entre os números digitados é {soma}')
