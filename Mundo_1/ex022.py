# ver vídeo de explicação no dia 20/02/2022
nome = input('Digite seu nome completo: ')
print(f'Seu nome com todas a letra maiúsculas fica assim:{nome.upper()}')
print(f'Seu nome com todas as letras minúsculas fica assim: {nome.lower()}')
espacos = nome.count(' ')
indice = len(nome)
print('Seu nome tem {} letras'.format(indice-espacos))
dividir = nome.split()
print(f'Seu primeiro nome tem: {len(dividir[0])} letras')
