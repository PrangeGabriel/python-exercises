sal = float(input('qual seu salario atual ?'))
if sal>=1250:
    sal = sal*1.1
else:
    sal = sal*1.15
print('seu novo salario é {:.2f} reais'. format(sal))
