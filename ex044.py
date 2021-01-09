valor = 450
cond = str(input('qual a condição de pagamento? \n dinheiro, cheque ou cartão'))
print(cond)
if cond == 'dinheiro' or cond == 'cheque':
    print('valor a pagar é de {}'.format(valor * 0.9))
elif cond == 'cartão':
    parc = int(input('vai pagar parcelado em quantas vezes? \n digite 1 se for a vista'))
    if parc == 1:
        print('o valor a pagar é de {} '.format(valor * 0.95))
    elif parc == 2:
        print('o valor fica em {} reais parcelado em {} vezes'.format((valor / parc), parc))
    elif parc >= 3:
        print('o valor parcelado é {} reais em {} parcelas '.format((valor * 1.2) / parc, parc))
