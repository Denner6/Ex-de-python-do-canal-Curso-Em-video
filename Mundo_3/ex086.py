numeros_da_matriz = [[], [], []]
index = 0
for i in range(1, 10):
    n = int(input(f'Digite o {i}º número: '))
    numeros_da_matriz[index].append(n)
    if i % 3 == 0:
        index += 1

print('-='*30)
for nums in numeros_da_matriz:
    for num in nums:
        print(f"[ {num:^5} ]", end="")
    print()
