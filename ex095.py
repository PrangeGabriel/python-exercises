dados = dict()
listaj = list()
camp = list()
somag = consulta = 0
while True:
    dados['nome'] = str(input('Nome do Jogador: '))
    np = int(input('Quantas partidas ele jogou? '))

    for n in range(0, np):
        gols = int(input(f'    fQual numero de gols na partida {n + 1}'))
        camp.append(gols)
        dados['partidas'] = camp[:]
        somag += gols

    dados['total'] = somag
    listaj.append(dados.copy())
    dados.clear()
    camp.clear()
    somag = 0
    resp = str(input('Deseja cadastrar mais algum jogador? [S/n]')).split()[0][0].upper()
    if resp in 'Nn':
        break
print(listaj)
print('*#' * 30, '\n')
print(f'{"cod":<5}{"nome":<12}{"gols":<15}{"total":<4}')
print('_' * 40)

for jog in listaj:
    print(f'{listaj.index(jog):<3}', end='')
    print(f'{jog["nome"]:<12}', end='')
    print(f'{str(jog["partidas"]):15}', end='')
    print(f'{jog["total"]:<4}', end='')
    print()
print('\n')
while True:
    consulta = int(input('Qual jogador gostaria de consultar o rendimento? [999 para sair]'))
    if consulta == 999:
        print('Obrigado por nada e volte nunca!')
        break
    if consulta > len(listaj):
        print('_-' * 40)
        print(f'Jogador não existe! Tente novamente, ou digite 999 para sair')
    else:
        print('_' * 40)
        print(f'Levantamento do jogador {listaj[consulta]["nome"]}')
        for partida, pos in enumerate(listaj[consulta]['partidas']):
            print(f'No jogo {partida+1} ele fez {pos} gols')
