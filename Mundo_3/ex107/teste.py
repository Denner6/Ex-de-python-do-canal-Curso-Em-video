from moeda import *
preco = float(input('Digite o preço: R$ '))

print(f'A metade de R${preco} é R${metade(preco)}')
print(f'O dobro de R${preco} é R${dobro(preco)}')
print(f'Aumentando em 10%, temos R${aumento(preco, 10)} ')
print(f"Diminuindo 13%, temos R${diminuir(preco, 13)}")

