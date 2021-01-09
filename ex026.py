frase = str(input('digite uma frase ')).upper().strip()
print('a letra A aparece {} vezes na frase'.format(frase.count('S')))
print('a primeira posição que a letra aparece é {} e a ultima é {}'.format(frase.find('S'),(len(frase)-frase[::-1].find('S'))))
