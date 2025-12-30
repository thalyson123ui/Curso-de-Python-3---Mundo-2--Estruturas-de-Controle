somaidade = 0
médiaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-----{} PESSOA -----'.format(p))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]:')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('a média de idade do grupo é de {} anos'.format(médiaidade))
print('o homem mais velho tem {} anos e se chama {}'.format(maioridadehomen, nomevelho))
print('ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))