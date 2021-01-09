num = int(input('digite um numero inteiro'))
opção = int(input('''escolha uma das bases para conversão:
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal'''))
if opção == 1:
    print('{} convertido para binario ´igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
