def notas(*num, sit=False):
    """

    :param num: adiciona notas numa tupla
    :param sit: situacao do aluno, se True, mostra se ele passou
    :return: retorna o boletim em forma de dicionario
    """

    soma = 0
    for c in num:
        soma += c

    media = soma / len(num)
    boletim = {'total': len(num), 'maior': max(num), 'menor': min(num), 'media': media}

    if sit:
        if media >= 7.0:
            boletim['situacao'] = 'Boa, vai passar'
        elif 6 <= media < 7:
            boletim['situacao'] = 'razoavel'
        else:
            boletim['situacao'] = 'RUIM mesmo, menino eh meio burro'

    return boletim


# programa principal
resp = notas(4.5, 8, 6.5, 5.0, sit=True)
print(resp)
