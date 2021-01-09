n1 = float(input('digite o lado 1'))
n2 = float(input('digite o lado 2'))
n3 = float(input('digite o lado 3'))
if n1< n2 + n3 and n2 < n3+n1 and n3<n2+n1:
    print('Da pra formar triangulo sim')
else:
    print('Nem da pra formar o triangulo')
