nome = str(input('digite o seu nome '))
cidade = str(input('digite o nome da cidade')).strip()
print('o nome da cidade começa com Santo? {}'.format('SANTO'in cidade.upper()))
print('o nome da pessoa é parente dos Silva? {}'.format('Silva' in nome))
