resp = 'S'
soma = cont = 0
maior = menor = quant = 0
while resp in 'Ss':
    numero = int(input('Digite um numero'))
    soma += numero
    cont += 1
    if cont == 1:
        numero = maior = menor
    else:
        if numero != 999:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
    resp = str(input('deseja continuar? [S/N]')).strip().upper()[0]
print('Foram digitados {} numeros e a soma deles é {}'.format(cont, soma))
print('a media dos valores é {}'.format(soma/cont))
print('o maior valor digitado é {}\n e o menor é {}'.format(maior, menor))
