listan = []
elc = 0
for seq in range(0, 5):
    elc = int(input('digite um numero de babalon'))
    if seq == 0 or elc > listan[-1]:
       listan.append(elc)
       print(f'adicionei o {elc} na ultima posição')
    else:
        for pos, valor in enumerate(listan):
            if  elc < valor:
                listan.insert(pos, elc)
                print(f'adicionei o valor {elc} na {pos}º posição')
                break


print(f'a lista em ordem sem utilizar sort fica {listan}')




    # for v in listan:
    #     print(f'o valor v é{v}, e o outro é {listan[v]}')
    #     if listan[v] < listan[len(listan)]:
    #         print(f'o ultimo valor é menor do que {listan[v]} na posição {v}')
    #     elif listan[v] > listan[len(listan)]:
    #         listan.insert(listan[v], listan[len(listan)])
    #         print(f'o indice {v}, e elemento {listan[v]}')
