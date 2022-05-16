n = float(input('Me informe qual a distância da sua viagem: '.strip()))
if n <=200:
    km = n * 0.50
    print(f'A passagem desta viagem custará R${km:.2f}')
else:
    km2 = n * 0.45
    print(f'A pasaagem desta viagem custará R${km2:.2f}')
print('Tenha uma boa viagem!!')