from datetime import date

nasc = int(input('qual seu ano de nascimento'))
idade = date.today().year - nasc
if idade < 18:
    print('ainda não esta na hora')
elif idade == 18:
    print('tá na hora de ir no quartel mandar gengeral tomar no cu')
else:
    print('sua idade é {} e já passou da hora de mandar milico se foder'.format(idade))
