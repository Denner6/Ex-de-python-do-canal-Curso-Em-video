dados = dict()
dados_lista = list()
media_idade = 0
mulheres_cadastradas = ''
while True:
    dados.clear()
    dados['Nome'] = input('Nome: ').title()
    dados['Sexo'] = input('Sexo: [M/F] ').upper()[0]
    while dados['Sexo'] != 'M' and dados['Sexo'] != 'F':
        print('Erro!, Por favor digite apenas M ou F')
        dados['Sexo'] = input('Sexo: [M/F] ').upper()[0]
    dados['Idade'] = int(input('Idade: '))
    dados_lista.append(dados.copy())
    continuar = input('Quer continuar? [S/N] ').lower()[0]
    while continuar != 's' and continuar != 'n':
        print('Erro, por favor digite apenas S ou N')
        continuar = input('Quer continuar? [S/N] ').lower()
    if continuar == 'n':
        break
for valor in dados_lista:
    media_idade += valor['Idade'] / len(dados_lista)
    if valor['Sexo'] == 'F':
        mulheres_cadastradas += valor['Nome']
        mulheres_cadastradas += ' '
print('-='*30)
print(f'Ao todo temos {len(dados_lista)} pessoas cadastradas.')
print(f'A média de idade é de {media_idade:.2f} anos.')
print(f'As mulheres cadastradas foram: {mulheres_cadastradas}')
print('Lista de pessoas que estão acima da média:')
for dicio in dados_lista:
    if dicio['Idade'] > media_idade:
        print('   ', end='')
        for key, valor in dicio.items():
            print(f'{key} = {valor}; ', end='')
        print()
print('>> Programa Encerrado <<')
