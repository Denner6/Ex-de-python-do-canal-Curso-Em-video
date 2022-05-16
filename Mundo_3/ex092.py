from datetime import datetime
dados = dict()
dados['Nome'] = input('Nome: ').title()
Nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - Nascimento
dados['Carteira de trabalho'] = int(input('Carteira de trabalho (\033[31m0\033[m não tem): '))

if dados['Carteira de trabalho'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Ano de contratação'] - Nascimento + 35
print('-='*30)
for key, valor in dados.items():
    print(f'{key} tem o valor \033[34m{valor}\033[m')
