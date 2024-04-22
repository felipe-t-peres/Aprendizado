nome = str(input('Digite seu nome completo: ')).strip()
print('\nSeu nome em maiúsculas: {}'.format(nome.upper()))
print('\nSeu nome em minúsculas: {}'.format(nome.lower()))
#como eu fiz
nomegrande=nome.replace(' ','')
print('\nSem os espaços seu nome tem {} letras!'.format(len(nomegrande)))

#Solução Professor
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

prnome = nome.split()
print('\nSeu primeiro nome é {} e tem {} letras'.format(prnome[0], len(prnome[0])))