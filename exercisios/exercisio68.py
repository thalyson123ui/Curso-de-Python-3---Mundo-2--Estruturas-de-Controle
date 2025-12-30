from random import randint
V = 0
while True:
    jogador = int(input('digs um valor: '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('par ou impar? [P/I] ')).strip().upper()[0]
    print(f'voce jogou {jogador} e o computador {computador}.total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCE VENCEU!')
            V += 1
        else:
            print('VOCE PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU!')
            V = 1
        else:
            print('VOCE PERDEU!')
            break
    print('vamos jogar novamente...')
print('GAME OVER! voce venceu {v} vezes.')