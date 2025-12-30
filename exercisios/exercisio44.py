print('{:=^40}'.format('LOJAS SILVA'))
preço = float(input('preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1]á vista dinheiro ou cheque
[2]á vista cartão
[3]2x no cartão
[4]3x ou mais no cartão''')
opção = int(input('qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('sua compra sera parcelada em 2x de R${:.2f} COM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('quantas parcelas? '))
    parcela = total / totparc
    print('sua compra dera parcelada em {}x de R${:.2f}'.format(totparc, parcela))
print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))