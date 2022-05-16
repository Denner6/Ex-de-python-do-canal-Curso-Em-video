salario = float(input('Digite seu salário: R$ '.strip()))
if salario >= 1250:
    aumento10 = salario * 0.10 + salario
    print(f'\033[1;34mVocê teve um aumento de 10%,então,seu salário apartir de agora é de\033[1;36m R${aumento10}')
else:
    aumento15 = salario * 0.15 + salario
    print(f'\033[1;34mVocê teve um aumento de 15%,então, seu salário apartir de agora é de\033[1;36m R${aumento15}')