from random import randint
computer = randint(0, 10)
i = 0
erros = 0
while i == 0:
    numero = int(input(
        'Tente adivinhar o número que estou pensando [Dica: Está entre 0 e 10]: '))
    if numero == computer:
        print(f'Parabéns! Você acertou!')
        break
    elif numero != computer:
        print(f'Oh no! Você errou! Tente novamente!')
        erros += 1
        continue

print(f'Você errou {erros} vezes antes de conseguir acertar.')
print(f'E o número que eu estava pensando era {computer}')
