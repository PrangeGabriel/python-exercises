a = float(input('digite o lado 1'))
b = float(input('digite o lado 2'))
c = float(input('digite o lado 3'))
if a + b > c and b + c > a and c + a > b:
    print('Da pra formar triangulo sim')
    if a != b and a != c and b != c:
        print('o triangulo é escaleno')
    elif a == b == c:
        print('triangulo equilatero')
    else:
        print('triangulo isosceles')
else:
    print('Nem da pra formar o triangulo')
