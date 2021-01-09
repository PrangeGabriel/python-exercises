c = ('\033[m',  # 0 sem cor
     '\033[0;30;41m',  # 1 vermelho
     '\033[0;30;42m',  # 2 verde
     '\033[0;30;45m',  # 3 roxo
     '\033[7;30m',     # 4 branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 3)
    print(c[4], end='')
    help(com)
    print(c[0],end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


# programa principal
comando = ''
while True:
    titulo('Sistema de ajuda PYhelp', 2)
    comando = str(input(' funcao ou biblioteca >> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ate nunca mais seu babaca!', 1)
