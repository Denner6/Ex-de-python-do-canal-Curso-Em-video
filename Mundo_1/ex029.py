velocidade = float(input('Digite sua velocidade: '.strip()))
if velocidade >80:
    print('MULTADO! Você foi multado por ultrapassar os limites de 80km/h!')
    multa = (velocidade-80)*7
    print(f'Você deve pagar uma multa de {multa:.2f}! ')
print("Dirija com segurança!")
