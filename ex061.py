p = int(input('Visualizador de PA, digite o primeiro termo'))
r = int(input('digite a razão da PA'))
c = 0
stop = 10
print(p)
while c < stop:
    print(p + r * c, end=' > ')
    c += 1
