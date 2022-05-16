from datetime import date
ano = int(input('Que ano quer analizar? Coloque 0 parta analizar o ano atual: '))
if ano % 4 ==0 and ano % 100!= 0 or ano % 400 == 0:
    ano = date.today().year
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')