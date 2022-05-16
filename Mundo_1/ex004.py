a = input('\033[30mDigite algo:')
print(f'\033[33mO tipo primitivo deste valor é \033[31m{type(a)} ')
print(f'\033[33mSó possui espaços? \033[31m{a.isspace()}')
print(f'\033[33mÉ um númerico? \033[31m{a.isnumeric()}')
print(f'\033[33mÉ alfabético? \033[31m{a.isalpha()}')
print(f'\033[33mÉ alfanumérico? \033[31m{a.isalnum()}')
print(f'\033[33mEstá tudo maiusculo? \033[31m{a.isupper()}')
print(f'\033[33mEstá tudo minúsculo? \033[31m{a.islower()}')
print(f'\033[33mEstá captalizada? \033[31m{a.istitle()}')


