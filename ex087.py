matriz = [[[], [], []], [[], [], []], [[], [], []]]
for linha in range(0, 3):
    for n in range(0, 3):
        matriz[linha][n] = int(input(f'Digite um numero para [{linha},{n}]'))

for linha in range(0, 3):

    for n in range(0, 3):
        print(f'[{matriz[linha][n]}]', end='')
    print('\n ')

