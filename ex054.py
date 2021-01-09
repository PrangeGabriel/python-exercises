from datetime import date
pessoas = 0
for c in range(0, 3):
    ano = int(input('digite o ano de nascimento'))
    if date.today().year - ano >= 18:
        print('ja completou')
        pessoas += 1
    else:
        print('não completou')
print(pessoas, 'já completaram a maioridade')
