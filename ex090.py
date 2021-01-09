aluno = dict()

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input(f'Qual a média de {aluno["nome"]}? '))


if aluno['média'] >= 7.0:
    print(f'a situação de {aluno["nome"]} é aprovada')
elif aluno['média'] < 7.0:
    print(f' infelizmente {aluno["nome"]} é burro')
