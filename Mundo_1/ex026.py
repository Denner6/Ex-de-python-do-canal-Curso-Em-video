frase = input('Escreva uma frase: ').upper().strip()
vez = frase.count('A')
print(f'Sua frase aparece a letra A {vez} vezes.')
frase2 = frase.find("A")+1
print(f'A primeira letra A apareceu na posição {frase2}')
frase3 = frase.rfind('A')+1
print(f'A letra A aparece or último na pósição {frase3}')