
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for contador in range(0, len(palavras)):
    print(
        f'\nNa palavra {palavras[contador].upper()} temos as vogais ', end=' ')
    for caracteres in palavras[contador]:

        if caracteres == 'a':
            print('a', end=' ')

        if caracteres == 'e':
            print('e', end=' ')

        if caracteres == 'i':
            print('i', end=' ')

        if caracteres == 'o':
            print('o', end=' ')

        if caracteres == 'u':
            print('u', end=' ')

print('\n')
