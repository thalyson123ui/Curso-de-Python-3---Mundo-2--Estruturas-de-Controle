print('gerador de PA')
print('-=' * 10)
primeiro = int(input('primeiro termo: '))
razão = int(input('razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -' .format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('quantos termos voce quer mostrar a mais? '))
print('FIM')
print('progressão finalizada com {} termos mostrados'.format(total))