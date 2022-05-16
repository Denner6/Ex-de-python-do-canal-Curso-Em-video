a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
if a<b and a<c:
    menor = a
    print(f'\033[1;30mO menor número é \033[1;36m {menor}')
if b<c and b<a:
    menor2 = b
    print(f'\033[1;30mO menor número é\033[1;36m {menor2}')
if c<b and c<a:
    menor3 = c
    print(f'\033[1;30mO menor número é\033[1;36m {menor3}')
if a>b and a>c:
    maior = a
    print(f'\033[1;30mO maior número é\033[1;36m {maior}')
if b>a and b>c:
    maior2 = b
    print(f'\033[1;30mO maior número é\033[1;36m {maior2}')
if c>a and c>b:
    maior3 = c
    print(f'\033[1;30mO maior número é\033[1;36m {maior3}')
