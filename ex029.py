
vel = float(input('Qual sua velocidade em km/h?'))
if vel > 80:
    print('''parabens! voce foi multado por excesso de velocidade!
          A multa irá custar {} reais'''.format((vel - 80)*7))
else:
    print('voce não foi multado :(')