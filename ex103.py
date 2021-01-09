def ficha(nome='<desconhecido>',gols=0):
    '''

    :param nome: nome do jogador
    :param gols: quantos gols ele fez
    :return:
    '''
    return f'o jogador {nome} fez {gols} no campeonato.'

print(ficha('paim', 6))
