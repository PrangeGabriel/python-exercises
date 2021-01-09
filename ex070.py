nome = fim = nomebarato = ''
preco = ptotal = contprodk = maisbarato = contcomp = 0
print('.:|:.' * 3, 'Supermercado BIG BALDE', '.:|:.' * 3)
while True:
    nome = str(input('QUal o nome do produto?'))
    preco = float(input(f'Qual o preço do {nome}?'))
    ptotal += preco
    contcomp += 1
    if preco > 1000:
        contprodk += 1
    if contcomp == 1:
        maisbarato = preco
        nomebarato = nome
    elif contcomp > 1:
        if preco < maisbarato:
            maisbarato = preco
            nomebarato = nome
    fim = str(input('Deseja continuar adicionando produtos? [Sim ou Não]'))
    if fim.strip().upper()[0] in 'Nn':
        break
print(f'O total gasto em compras foi de R$ {ptotal:.2f}'
      f'\n Foram um total de {contprodk} produtos acima de R$1000,00'
      f'\n o nome do produt mais barato é {nomebarato} custando R${maisbarato}')
