def metade(numero):
    return numero / 2


def dobro(numero):
    return numero * 2


def aumento(numero, porcentagem):
    return numero + (porcentagem / 100) * numero


def diminuir(numero, porcentagem):
    return numero - (porcentagem / 100) * numero


def moeda(numero):
    return f'R${numero:.2f}'.replace('.', ',')
