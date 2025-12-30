soma = cont = 0
while True:
    num = int(input('digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'a soma dos {cont} valores foi {soma}')