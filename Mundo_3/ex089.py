geral = []
while True:
    nome = input('Nome: ').title()
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media =(nota_1 + nota_2) / 2
    geral.append([nome, [nota_1, nota_2], media])
    continuar = input('Quer continuar? [S/N] ').lower()
    if continuar == 'n':
        break

print('-='*30)
print('Nº   NOME        MÉDIA')
print('-'*30)

for i, aluno in enumerate(geral):
    print(f'{i:<4} {aluno[0]:<10} {aluno[2]:>8.2f}')
print('-'*30)

while True:

    mostrar_notas = int(input('Quer que eu mostre a nota de qual aluno? (999 interrompe): '))

    if mostrar_notas >= len(geral) - 1:
        print(f'Notas do(a) {geral[mostrar_notas][0]} são {geral[mostrar_notas][1]} e a média é {geral[mostrar_notas][2]:.2f} ')
        print('-'*30)

    if mostrar_notas == 999:
            print('Finalizando programa...')
            print('PROGRAMA ENCERRADO!')
            break
