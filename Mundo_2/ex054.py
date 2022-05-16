from datetime import date
ano = date.today().year  # ESSE ANO TAVA DANDO ERRO

lista = []
maiores = 0
menor = 0

for i in range(1, 8):  # COM O ANO QUE TAVA AQUI
    nascimento = int(input(f'Informe o ano de nascimento  da {i}º pessoa: '))
    lista.append(nascimento)

for nascimento in lista:
    idade = ano - nascimento  # AI AQUI TAVA PEGANDO O VALOR DO RANGE DE CIMA
    if idade >= 21:
        maiores += 1
    else:
        menor += 1


print(f'{menor} pessoas são menores de 18 anos')
print(f'{maiores} pessoas já atingiram a maioridade')
