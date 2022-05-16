dados = dict()
lista_de_gols = list()
dados_dos_jogadores = list()
while True:
    dados.clear()
    print('-'*30)
    dados['Nome do jogador'] = input('Nome do jogador: ').title()
    partidas_jogadas = int(input(f'Quantas partidas {dados["Nome do jogador"]} jogou? '))
    for i in range(0, partidas_jogadas):
        lista_de_gols.append(int(input(f'  Quantos gols na partidas {i+1}? ')))
        dados['Gols'] = lista_de_gols[:]
    lista_de_gols.clear()
    dados_dos_jogadores.append(dados.copy())
    continuar = input('Quer continuar? [S/N] ').lower()
    while continuar != 'n' and continuar != 's':
        print('Erro digite somente S ou N')
        continuar = input('Quer continuar? [S/N] ').lower()

    if continuar == 'n':
        break
print('-='*30)
print(f'{"Cód":<4} {"Nome":<15} {"Gols":<15} {"Total":<15}')
print('-'*43)
for i, valor in enumerate(dados_dos_jogadores):
    print(f'{i:<3}  {valor["Nome do jogador"]:<15} {", ".join(map(str,valor["Gols"])):<15} {sum(valor["Gols"]):<15} ')
print('-'*43)

while True:
    mostrar_dados = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    if mostrar_dados == 999:
        break
    if mostrar_dados <= len(dados_dos_jogadores) - 1:
        print(f'-- Levantamento do jogador {dados_dos_jogadores[mostrar_dados]["Nome do jogador"]}:')
        for i, gols in enumerate(dados_dos_jogadores[mostrar_dados]['Gols']):
            print(f'  → Na partida {i+1} fez \033[33m{gols}\033[m gols ')
        print(f'Totalizando \033[33m{sum(dados_dos_jogadores[mostrar_dados]["Gols"])}\033[m gols')
    else:
        print('Código não encontrado,tente novamente')

print('Finalizando programa...')
print('Programa encerrado, Volte sempre!')

