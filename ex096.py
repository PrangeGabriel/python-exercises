def area(larg, comp):
    a = larg * comp

    print(f'A area de um terreno {larg} x {comp} é de {a}m²')


# programa principal
print(f''' ----------------------
            CONTROLE DE TERRENOS
            ---------------------''')
l = float(input('Largura (m):  '))
c = float(input('Comprimento (m): '))
area(l, c)
