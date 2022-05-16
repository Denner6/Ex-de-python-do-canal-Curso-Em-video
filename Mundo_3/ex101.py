def voto(birth):
    from datetime import date
    idade_atual = date.today().year - birth
    if 18 <= idade_atual < 65:
        return f'Com {idade_atual} anos: Voto OBRIGATÓRIO'
    elif idade_atual < 18:
        return f'Com {idade_atual} anos: NÃO VOTA'
    elif idade_atual >= 65:
        return f'Com {idade_atual} anos: Voto OPCIONAL '

# Main program
print('-'*30)
ano_de_nascimento = int(input('Em que ano você nasceu? '))
print(voto(ano_de_nascimento))
