import colorama
colorama.init()
print(f'========== Loja do Young ==========')
preço_do_produto = float(
    input('Me informe o preço das compras:\033[32mR$\033[m').strip())
print('''FORMA DE PAGAMENTO
\033[34m[ 1 ]\033[mÁ vista (dinheiro ou cheque), 10% de desconto,
\033[34m[ 2 ]\033[mÁ vista (cartão), 5% de desconto,
\033[34m[ 3 ]\033[mEm até 2x no cartão, preço normal,
\033[34m[ 4 ]\033[mEm até 3x ou mais no cartão, 20% de juros.''')
forma_de_pagamento = int(input('Informe a forma de pagamento:').strip())

if forma_de_pagamento == 1:
    print(
        'Forma de pagamento selecionada: [ 1 ]Á vista (Dinheiro), desconto de 10%')
    desconto = preço_do_produto - preço_do_produto * 10 / 100
    print(f'Você deverá pagar \033[32mR${desconto:.2f}\033[m')

elif forma_de_pagamento == 2:
    print(
        'Forma de pagamento selecionada: [ 2 ]Á vista (cartão),  desconto de 5%  ')
    desconto = preço_do_produto - preço_do_produto * 5 / 100
    print(f'Você deverá pagar \033[32mR${desconto:.2f}\033[m')

elif forma_de_pagamento == 3:
    parcela = preço_do_produto / 2
    print(
        'Forma de pagamento selecionada: [ 3 ]Em até 2x no cartão, preço normal  ')
    print(f'Sua compra foi parcelada em 2x de R${parcela:.2f} SEM JUROS ')

elif forma_de_pagamento == 4:
    parcelas = int(input('Quantas parcelas?').strip())
    print(
        'Forma de pagamento selecionada: [ 4 ] Em até 3x ou mais no cartão, 20% de juros')
    juros = preço_do_produto * 20 / 100 + preço_do_produto
    parcelas2 = juros / parcelas
    print(f'''
Sua compra será parcelada em \033[35m{parcelas}x\033[m de \033[32mR${parcelas2:.2f}\033[m por conta do juros de 20%.
Sua compra de \033[32mR${preço_do_produto:.2f}\033[m vai custar \033[32mR${juros:.2f}\033[m no final, por conta dos juros de 20%.
    ''')

else:
    print('\033[31mOpção inválida!')
