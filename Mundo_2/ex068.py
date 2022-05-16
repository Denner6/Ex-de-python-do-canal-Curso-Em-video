from random import randint

print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)

venceu = 0

while True:
    valor = int(input('Diga um valor: '))
    par_impar = str(input('Você quer PAR ou ÍMPAR? [P/I] '))
    computer = randint(0, 10)
    computer2 = 'i' if par_impar == 'p' else 'p'
    print('-='*20)
    soma = valor + computer

    if soma % 2 == 0:
        print(
            f'Você jogou {valor} e o computador {computer}. E o total foi {soma} ou seja PAR')
        print('-='*20)
    else:
        print(
            f'Você jogou {valor} e o computador {computer}. E o total foi {soma} ou seja ÍMPAR')
        print('-='*20)

    if soma % 2 == 0 and par_impar.lower() == 'p':
        if computer2 == 'i':
            print(f'Você VENCEU!')
            print('Vamos jogar novamente... ')
            venceu += 1
            print('-='*20)

    elif soma % 2 == 0 and par_impar.lower() == 'i':
        if computer2 == 'p':
            print(f'Você PERDEU!')

        break

    elif soma % 2 == 1 and par_impar.lower() == 'i':
        if computer2 == 'p':
            print(f'Você VENCEU!')
            print('Vamos jogar novamente... ')
            venceu += 1
            print('-='*20)

    elif soma % 2 == 1 and par_impar.lower() == 'p':
        if computer2 == 'i':
            print('Você PERDEU!')
        break

print(f'GAME OVER! Você venceu {venceu} vezes')
print('-='*20)
# if valor == '' or ' ':
#print('Opção Inválida. Tente novamente.')
# sleep(2)
# elif par_impar.lower() != 'p' or par_impar.lower() != 'i':
#  print('Opção Inválida. #Tente novamente.')
# sleep(1.5)
# Resolver amanha, fazendo mais dois elif
