def lerInteiro(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print(f"\033[31mERRO: Por favor digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não informar esse número.\033[m')
            return 0
        else:
            return inteiro


def lerfloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print(f"\033[31mERRO: Por favor digite um número real válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não informar esse número.\033[m')
            return 0
        else:
            return real



inteiro = lerInteiro('Digite um inteiro: ')
real = lerfloat('Digite um real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')

