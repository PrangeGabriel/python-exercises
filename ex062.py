p = int(input('Visualizador de PA, digite o primeiro termo'))
r = int(input('digite a razão da PA'))
c = 0
stop = 10
print('Os dez primeiros termos da progressão aritmética são:')
while c < stop:
    print(p + r * c, end=' > ')
    c += 1
stop = 10 + int(input('\n\nQuer mostrar mais termos da PA? digite quantos, ou digite [0] para sair'))
while stop != 0:
    if stop != 0:
        while c < stop:
            print(p + r * c, end=' > ')
            c += 1
    else:
        print('Programa finalizado')
