def ficha(jogador, gols):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols.isalpha() or gols == '':
        gols = 0
    return f'O jogador {jogador} marcou {gols} gol(s) no campeonato'


# Main program
print('-'*30)
nome_do_jogador = input('Nome do jogador: ').title().strip()
numero_de_gols = input('Número de gols: ').strip()
print(ficha(nome_do_jogador, numero_de_gols))

