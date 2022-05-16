i = 0
while i == 0:
    sexo = input('Informe seu gênero [M/F]:').lower()
    if sexo != 'm' and sexo != 'f':
        if sexo == 'j':
            print('🐢 Você é do gênero jabuti?Tente novamente 🐢')
        print('Opção invalida, Tente novamente:')
        continue
    if sexo == 'm':
        print('Você é do sexo masculino!')

    if sexo == 'f':
        print('Você é do sexo feminino!')
    break


print('FIM')
