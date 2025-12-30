print('-' * 30)
print('{:^30}'.format('banco thalyson ltda'))
print('-' * 30)
valor = int(input('qu valor voce quer sacar? R$'))
total = valor
ced = 50
totcéd = 0
while True:
    if total >= ced:
        total -= ced
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'total de {totcéd} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total = 0
        if total == 0:
            break
print('=' * 30)
print('volte sempre!')