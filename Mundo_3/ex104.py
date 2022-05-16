def ler_inteiro(msg):
    enviar = input(f'{msg}').strip()
    while not enviar.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        enviar = input(f'{msg} ').strip()
    return f'Você acabou de digitar o número {enviar}'


# Main program
print(ler_inteiro('Digite um número: '))
