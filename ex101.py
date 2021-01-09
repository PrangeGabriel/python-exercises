def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 16 <= idade < 65:
        resp = 'voto obrigatorio'
        return idade, resp
    elif 16 > idade:
        resp = 'voto proibido'
        return idade, resp
    elif idade >= 65:
        resp = 'voto opcional'
        return idade, resp

    # #outra maneira de escrever
    # if idade < 16:
    #     return f'Com {idade} anos: Nao vota'
    # elif 16<= idade <18 or idade >65:
    #     return f' com {idade} anos : VOTO OPCIONAL.'
    # else:
    #     return f' Com {idade} anos : VOTO OBRIGATORIO'

situacao = voto(int(input('Digite o ano de nascimento: ')))
print(f'com {situacao[0]} anos a situacao da pessoa se deu como: {situacao[1]}')
