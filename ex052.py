n = int(input('digite o numero para saber se é primo'))
t = 0
for c in range(2, n):
    if n % c == 0:
        t += 1
if t >= 1:
    print('\033[34m', n, 'não é primo')
else:
    print('\033[31m', n, 'é primo')

print(t, 'é o numero de divisores possiveis')
