def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um numero e caso show seja True, mostra o calculo na tela.
    :param num: o numero a ser calculado
    :param show: (opcional) Mostrar ou nao a conta
    :return: o valor do Fatorial de um numero num
    """
    fat = 1
    for c in range(num, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(f' x ',end='')
            else:
                print(f' = ',end='')
        fat *= c
    return fat

#programa principal

print(fatorial(5, True))