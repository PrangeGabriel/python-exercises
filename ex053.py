frase = str(input('digite a frase')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('a frase é palindromo')
else:
    print('não é palindromo')
