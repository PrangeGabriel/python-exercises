massa = float(input('digite sua massa em kg'))
alt = float(input('digite sua altura em m '))
imc = massa / alt ** 2
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 < imc < 25:
    print('peso ideal')
elif 25 < imc < 30:
    print('sobre peso')
elif 30 < imc < 40:
    print('fat sonic')
else:
    print('obesidade morbida')
