from random import randint
itens = ('pedra','papel','tesoura')
computador = randint(0, 2)
print('o computador escolheu {}'.format(itens [computador]))
print('''suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('qual é a sua jogada? '))
print('-=' * 20)
print('computador jogou {}'.format (itens [computador]))
print('jogador jogou {}'.format(itens [jogador]))
print('-=' * 20)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!')