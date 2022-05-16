from time import sleep
from pygame import mixer

print('Lançamento do foguete em')
for l in range(10, -1, -1):
    print(l)
    sleep(1)
print('Lançamento iniciado.')
print('[1] Sim\n[2] Não')
explosao = int(input('Gostaria de explodir os fogos?'))
if explosao == 1:
    print('Os fogos serão acesos em ')
    for a in range(3, -1, -1):
        print(a)
        sleep(1)
    print('🎆 FOGOS ACESOS! 🎆')

    import pygame

    pygame.mixer.init()

    pygame.init()  # essa inicialização nos meus testes, não foi necessária

    pygame.mixer.music.load('ex046.mp3')

    pygame.mixer.music.play()

    pygame.mixer.music.set_volume(1)

    x = input('Digite algo para encerrar ...')


elif explosao == 2:
    print(f'Os fogos NÃO foram acesos')
else:
    print('✖ Opção inválida.Tente novamente')
