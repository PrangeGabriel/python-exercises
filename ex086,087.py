matriz = [[[], [], []], [[], [], []], [[], [], []]]
soma = outrasoma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um numero para [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if c == 2:
            outrasoma += matriz[l][c]
    print()

print(f'A soma de todos os valores pares digitados é {soma}')
print(f'A soma dos valores da terceira coluna é {outrasoma}')
print(f'o maior valor da segunda linha é {max(matriz[1])}')
