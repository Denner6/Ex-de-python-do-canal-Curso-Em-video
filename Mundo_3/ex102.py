def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número
    :param numero: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: Valor do fatorial de um número n
    """
    f = 1

    for num in range(numero, 0, -1):
        if show:
            print(f'{num} ', end='')
            print(f'✗ ' if num > 1 else '= ', end='')
        f *= num
    return f


f1 = fatorial(6, show=True)
print(f1)

