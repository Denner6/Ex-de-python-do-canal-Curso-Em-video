print('-'*20)
print('LOJÃO DO YOUNG')
print('-'*20)

total_gasto = []
produtos_que_custam_mais_de_1000 = 0
mais_barato = 999999999
preco_do_mais_barato = []

while True:
    nome = input('Nome do produto: ').title()
    preco = float(input('Preço:R$').strip())
    continua = input('Quer continuar? [S/N] ').lower()
    print('-'*20)

    preco_do_mais_barato.append(preco)
    menor = min(preco_do_mais_barato)
    total_gasto.append(preco)
    soma = sum(total_gasto)

    if preco > 1000:
        produtos_que_custam_mais_de_1000 += 1

    if preco < mais_barato:
        mais_barato = preco
        X = nome
    if continua == 'n':
        break
    while continua != 's' and continua != 'n':
        continua = input('Quer continuar? [S/N] ').lower()
print('-'*20)
print(f'FIM DO PROGRAMA')
print('-'*20)
print(f'O total da compra foi R${soma:.2f}')
print(
    f'Temos {produtos_que_custam_mais_de_1000} produtos que custam mais de R$1000.00')
print(
    f'O produto mais barato foi {X} que custou R${menor:.2f}')
