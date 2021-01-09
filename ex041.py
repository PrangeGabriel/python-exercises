from datetime import date

nasc = int(input('digite o ano de seu nascimento '))
idade = date.today().year - nasc
if idade < 9:
    print('tu é juvenil demais, só {} anos '.format(idade))
elif idade < 14:
    print('muito infanto juvenil')
elif idade < 19:
    print('mc junior ')
else:
    print('ai tu ja ficou velho demais')
