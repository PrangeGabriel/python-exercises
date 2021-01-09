valores = list()
for v in range(0, 5):
    valores.append(int(input('digite algo para armazenar')))
for c, v in enumerate(valores):
    print(f'o {c + 1}º valor digitado foi de {v}')
print(f'e o maior e menor valor foram de {max(valores)} e {min(valores)}')

print(f'os maiores valores digitados foram de {max(valores)} nas posições ', end=' ')
for indice, valores in enumerate(valores):
    if valores == max(valores):
        print(f'{indice}...')

print(f'os menores valores digitados foram de {min(valores)}, nas posições ', end=' ')
for indice, valores in enumerate(valores):
    if valores == min(valores):
        print(f'{indice}...')
