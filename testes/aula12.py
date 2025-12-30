nome = str(input('qual é o seu nome? '))
if nome == 'thalyson':
    print('que nome bonito!')
elif nome == 'joaquina' or nome == 'nathan' or nome == 'cesar':
 print('seu nome é bem popular na sua familia')
elif nome in 'ana lucia':
 print('belo nome feminino voce tem')
else:
 print('seu nome é um nome normal hoje em dia')
print('tenha um bom dia {}'.format(nome))