def metade(numero=0, formatar=False):
    resp = numero / 2
    return resp if not formatar else moeda(resp)


def dobro(numero=0, formatar=False):
    resp = numero * 2
    return resp if not formatar else moeda(resp)


def aumento(numero=0, porcentagem=0, formatar=False):
    resp = numero + (porcentagem / 100) * numero
    return resp if not formatar else moeda(resp)


def diminuir(numero=0, porcentagem=0, formatar=False):
    resp = numero - (porcentagem / 100) * numero
    return resp if not formatar else moeda(resp)


def moeda(numero):
    return f'R${numero:.2f}'.replace('.', ',')


def resumo(numero=10, aumentar=15, reduzir=30):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analizado: \t{moeda(numero)}')
    print(f'Dobro do preço: \t{dobro(numero, True)}')
    print(f'Metade do preço: \t{metade(numero, True)}')
    print(f'{aumentar}% de aumento: \t{aumento(numero, aumentar, True)}')
    print(f'{reduzir}% de redução:  	{diminuir(numero, reduzir, True)}')
    print('-'*30)
