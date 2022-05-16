def area(x, y):
    calcular_area = x * y
    print(f'A área de um terreno de {x} x {y} é de {calcular_area}m²')


# Programa principal
print("Controle de terrenos")
print('-'*20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m):'))
area(largura, comprimento)
