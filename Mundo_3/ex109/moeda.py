def metade(numero, formatar=False):
    resp = numero / 2
    return resp if not formatar else moeda(resp)

def dobro(numero, formatar=False):
    resp = numero * 2
    return resp if not formatar else moeda(resp)


def aumento(numero, porcentagem, formatar=False):
    resp = numero + (porcentagem / 100) * numero
    return resp if not formatar else moeda(resp)


def diminuir(numero, porcentagem, formatar=False):
    resp = numero - (porcentagem / 100) * numero
    return resp if not formatar else moeda(resp)


def moeda(numero):
    return f'R${numero:.2f}'.replace('.', ',')
