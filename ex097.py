def escreva(txt):
    tam = int(len(txt) + 4)
    print('~' * tam)
    print(f'  {txt}')
    print('§' * tam)


# programa principal

texto = 'Curso em Video aasdadasda'
escreva(texto)

texto = str(input('digite a mensagem'))
escreva(texto)
