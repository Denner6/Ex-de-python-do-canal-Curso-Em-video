a1 = int(input("Primeiro termo: ").strip())
r = int(input('Razão: ').strip())
decimo = a1+(10 -1)*r
for c in range(a1,decimo,r):
    print(f'{c}',end='  ➔  ')
print('ACABOU')
