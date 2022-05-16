from datetime import date
ano = date.today().year
nascimento = int(input('Ano de nascimento: ').strip())
idade =  ano - nascimento
print(f'Quem nasceu no ano {nascimento} tem {idade} anos  em {ano}')
if idade == 18:
    print('Você deve se alisatar IMEDIATAMENTE')
elif idade < 18:
    saldo =  18 - idade
    qnt = ano + saldo
    print(f'Ainda faltam {saldo} anos para o alistamento')
    print(f'Seu alistamento será em {qnt}')
elif idade > 18:
    saldo = idade - 18
    qnt = ano - saldo
    print(f'Você deveria ter se alistado a {saldo2} anos. Espero que já tenha se alistado. ')
    print(f'Seu alistamento devia ter sido a {qnt} anos')
