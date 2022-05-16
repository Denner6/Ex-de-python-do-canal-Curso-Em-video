teste = input('Digite uma expressão:')

lista = []

for c in teste:
    if c == '(':
        lista.append(teste)
    elif c == ')':
        if len(lista) > 0 :
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista)== 0:
    print('Sua expressão está valida')
else:
    print('sua expressão está invalida')
