tuplap = ('aprender', 'programar', 'linguagem', 'python', 'curso',
         'gratis', 'estudar', 'praticar', 'trabalhar',
         'mercado', 'prorgamador', 'futuro')
for palavras in tuplap:
    print(f'\nna palavra {palavras.upper()} temos:', end='')
    for letra in palavras:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
