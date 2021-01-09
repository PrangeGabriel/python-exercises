num = cont = soma = 0
while True:
    num = int(input('Digite um numero para somar ou digite [999] para sair'))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} numeros cuja soma vale {soma}')
print('Programa finalizado')
