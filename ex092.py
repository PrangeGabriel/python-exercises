from datetime import date

pessoa = dict()
pessoa['nome'] = str(input('Nome:'))
anonasc = int(input('Ano de nascimento '))
pessoa['idade'] = date.today().year - anonasc
pessoa['CTPS'] = int(input('Nº da Carteira de Trabalho [0 se não existir] '))


if pessoa['CTPS'] > 0:
    pessoa['contrato'] = int(input('Ano da contratação: '))
    pessoa['salario'] = int(input('Salario base: '))
    pessoa['aposentadoria'] = 35 - (date.today().year - pessoa['contrato']) + pessoa['idade']

print(pessoa)

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
