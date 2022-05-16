print('\033[30m-=\033[m'*20)
print('\033[30mAnalizador de triângulos\033[m')
print('\033[30m-=\033[m'*20)
r1 = float(input('\033[30mPrimeiro segmento: '))
r2 = float(input('\033[30mSegundo segmento: '))
r3 = float(input('\033[30mTerveiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;32mOs segmentos acima, PODEM FORMAR um TRIÂNGULO.')
else:
    print('\033[1;31mOs segmentos acima, NÃO PODEM FORMAR um TRIÂNGULO.')
