nome = ''
idade = 0
sexo = 0
media = 0
lhermu = 0
for c in range(1,5):
    print('{}ª pessoa'.format(c))
    idade = int(input('qual sua idade'))
    media += idade/4
    nome = str(input('qual seu nome')).strip()
    sexo = str(input('qual seu genero?')).strip()
    if sexo == 'mulher' and idade <20:
        lhermu +=1
print(media, 'é a media de idade do grupo')
print('{} são o numero de mulheres abaixo de 20 anos')
