lista = [[], []]
num = 0

for seq in range(0, 7):
    num = int(input(f'joga o {seq} numero ai'))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista.sort()
print(f'os valores pares em orde crescente foi de {lista[0]}')
print(f'e os impares em ordem crescente foi de {lista[1]}')
