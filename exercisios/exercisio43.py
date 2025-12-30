peso = float(input('qual é seu peso? (kg)'))
altura = float(input('qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('o IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('voce esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABENS, voce esta na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('voce esta em SOBREPESO')
elif 30 <= imc < 40:
    print('voce esta em OBESIDADE!')
elif imc >= 40:
    print('voce esta em OBESIDADE MORBIDA,cuidado!')