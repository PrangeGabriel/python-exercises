p = int(input('digite o primeiro termo da Progressao Aritmetica'))
r = int(input('digite a razão da PA'))
decimo = p + (10 - 1)* r
print('os 10 primeiros termos da Progressão Arirtmetica são')
for c in range(p, decimo+r, r):
    print('{}'.format(c), end=' > ')
print('fim')
