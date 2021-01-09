listalu = []
while True:
    nome = str(input('digite o nome do aluno:'))
    nota1 = float(input('digite a nota 1: '))
    nota2 = float(input('digite a nota 2: '))
    media = (nota1 + nota2) / 2
    listalu.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar ? [S/n]'))
    if resp in 'Nn':
        break

print(listalu)
print('+=' * 20)
print(f'{"Nº":<4}{"NOME":<13}{"MEDIA":>8}')
for indice, aluno in enumerate(listalu):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    opc = int(input('Mostar notas de qual aluno/ 999 para interromper'))
    if opc == 999:
        break
    if opc <= len(listalu) - 1:
        print(f' notas de {listalu[opc][0]} são {listalu[opc][1]}')
