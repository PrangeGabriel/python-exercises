dados = dict()
dados['nome'] = str(input('Nome do Jogador: '))
np = int(input('Quantas partidas ele jogou? '))
camp = list()
for n in range(0, np):
    camp.append(int(input(f'Qual numero de gols na partida {n + 1}')))
    dados['partidas'] = camp[:]
somag = 0
for p in camp:
    somag += p

dados['total'] = somag
print(dados, '\n')
print('*#' * 30, '\n')

for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')

print('#@' * 32)
print(f'O jogador {dados["nome"]} jogou {len(camp)} partidas.')
for pos, gol in enumerate(camp):
    print(f'Na partida {pos}, fez {gol} gols. ')
