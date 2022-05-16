frase = input('Digite uma frase: ').lower()
lista = frase.split()
for i in lista:
    fraseInvertida = frase[::-1]
if frase == fraseInvertida:
    fraseInvertida.replace(' ', '')
    print(
        f'Essa frase é um PALÍNDROMO.\nE ao contrario ela fica assim:\n{fraseInvertida}')
else:
    print(f'Essa frase NÃO é um PALÍNDROMO.')
