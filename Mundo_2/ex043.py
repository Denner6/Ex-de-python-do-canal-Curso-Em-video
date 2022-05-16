peso = float(input('Me informe seu peso:(Kg) '))
altura = float(input('Me informe sua altura:(M) '))
Imc = peso / altura ** 2
print(f'Seu Imc é de {Imc:.1f} kg')
if Imc < 18.5:
    print('Você está ABAIXO do peso ideal.')
elif  Imc <= 25:
    print('Você está no PESO IDEAL.')
elif Imc <= 30:
    print('Você está com SOBREPESO')
elif  Imc <= 40:
    print('Você está OBESO')
else:
    print('Você está em Obesidade MÓRBIDA')