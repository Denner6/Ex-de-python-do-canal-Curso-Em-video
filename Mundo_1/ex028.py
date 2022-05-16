import random
n = int(input('Tente adivinhar o número que estou pensando(Dica é entre 0 e 5): '.strip()))
aleatório = random.randint(0,5)
if n == aleatório:
    print(f'Você acertou! O número que estou pensando é {aleatório}')
else:
    print(f'Oh no! Você errou! O número que eu estava pensando era {aleatório}')


