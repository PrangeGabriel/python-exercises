from datetime import datetime

idade = contidade = sexo = contsexo = mulher = 0
fim = ''
hoje = datetime.today().year
print('\033[7m=+' * 5, 'Cadastro de pessoas', '+=' * 5, '\033[m')
while True:
    idade = int(input('Digite a idade da pessoa'))
    sexo = str(input('Qual o genero que a pessoa se identifica? [Homem ou Mulher}'))
    fim = str(input('Deseja cadastrar mais alguem? [Sim ou Não]'))
    if idade > 18:
        contidade += 1
    if sexo.strip().upper()[0] in 'Hh':
        contsexo += 1
    if sexo.strip().upper()[0] in 'Mm' and idade < 20:
        mulher += 1
    if fim.strip().upper()[0] in 'Nn':
        break
print(f'{contidade} pessoas tem mais de 18 anos\n'
      f'{contsexo} homens foram cadastrados\n'
      f'{mulher} mulheres tem menos de 20 anos)')
