n = int(input('Digite um número: ').strip())
print('Escolha uma forma de converção de acordo com a tabela abaixo: ')
print('\033[34m[ 1 ] \033[mPara Binário ')
print('\033[34m[ 2 ] \033[mPara Octal')
print('\033[34m[ 3 ] \033[mPara Hexadecimal')
converção = input('Digite o número de converção que deseja: ')
binário = bin(n)[2:]
octal = oct(n)[2:]
hexa = hex(n)[2:]

if converção == '1': #Obs: Também pode ser feito em número e não só em string.
    print(f'\033[mO número \033[35m{n} \033[mna forma BINÁRIA é \033[36m{binário}.')
elif converção == '2':
    print(f'\033[mO número \033[35m{n} \033[mna forma OCTAL é \033[36m{octal}')
elif converção == '3':
    print(f'\033[mO número \033[35m{n} \033[mna forma HEXADECIMAL é \033[36m{hexa}')
else:
    print('\033[31m❌ \033[mOpção inválida!')

