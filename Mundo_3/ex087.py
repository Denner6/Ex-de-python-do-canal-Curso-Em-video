numeros_da_matriz = [[], [], []]
soma_pares = 0
soma_terceira_coluna = 0
index = 0
maior_valor_da_segunda_linha = 0
l = 0
c = 0
for i in range(1, 10):
    n = int(input(f'Digite o {i} valor: '))
    
    numeros_da_matriz[index].append(n)
    if i % 3 == 0:
        index += 1

print('-='*30)
for nums in numeros_da_matriz:

    numero_final = int(nums[-1])
    if nums[-1]:
        soma_terceira_coluna += numero_final

    for num in nums:

        #Soma dos ímpares

        if nums == numeros_da_matriz[1]:
            if maior_valor_da_segunda_linha is None or num > maior_valor_da_segunda_linha:
                maior_valor_da_segunda_linha = num

        #Soma dos pares

        if num % 2 == 0:
            soma_pares += num

        print(f"[ {num:^5} ]", end="")
    print()


print('-='*30)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_valor_da_segunda_linha}')
