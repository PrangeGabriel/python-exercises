n1 = float(input('qual a nota da primeira prova? '))
n2 = float(input('qual a nota da segunda prova? '))
media = (n1 + n2) / 2
if media < 5.0:
    print('se fudeu', media)
elif 5.0 < media < 6.9:
    print('recuperação sempre com media ', media)
else:
    print('aprovado com media ', media)
