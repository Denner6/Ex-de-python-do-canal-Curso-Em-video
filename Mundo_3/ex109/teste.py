from ex109 import moeda
preco = float(input('Digite o preço: R$ '))


print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando em 10%, temos {moeda.aumento(preco, 10, True)} ')
print(f"Diminuindo 13%, temos {moeda.diminuir(preco, 13, True)}")

