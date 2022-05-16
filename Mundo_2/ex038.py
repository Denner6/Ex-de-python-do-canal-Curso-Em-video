n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O \033[33mPRIMEIRO\033[m número é maior')
elif n2 > n1:
    print('O \033[33mSEGUNDO\033[m número é maior')
elif n1 == n2:
    print('\033[31mNÃO TEM\033[m número maior, ambos tem o mesmo valor')
#também pode usar else: em vez de elif no final