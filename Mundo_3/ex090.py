dados = dict()
dados['Nome'] = input('Nome: ').title()
dados['Média'] = float(input(f'Média de {dados["nome"]}: '))
print('-='*20)
if 5 <= dados['Média'] < 7:
    dados['Situação'] = 'Recuperação'

elif dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'

else:
    dados['Situação'] = 'Reprovado'

for k,v in dados.items():
    print(f'     - {k} é igual a {v}')
