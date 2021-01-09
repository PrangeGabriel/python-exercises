resp = str(input('Digite seu sexo biologico [M/F]')).upper().strip()[0]
while resp not in 'MmFf':
    resp = str(input('Digitação errada, tente novamente.\n Qual seu sexo biologico? [M/F]')).upper()
    if resp != 'M' and resp != 'F':
        print('digitação errada')
    else:
        print('resposta validada')

