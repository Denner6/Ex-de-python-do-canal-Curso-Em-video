r1 = float(input('Primeiro segmento: ').strip())
r2 = float(input('Segundo segmento:').strip())
r3 = float(input('Terceiro segmento:').strip())

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;32mOs segmentos acima, PODEM FORMAR um TRIÂNGULO.\033[m')
    if r1 == r2 ==r3:
        print('Esse triângulo é um triângulo \033[33mEQUILÁTERO\033[m')
    elif r1 != r2 != r3 != r1:
        print('Esse triângulo é \033[35mESCALENO\033[m')
    else:
        print('Esse triângulo é \033[34mISÓSCELES\033[m')
else:
    print('\033[1;31mOs segmentos acima, NÃO PODEM FORMAR um TRIÂNGULO.')