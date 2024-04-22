n1 = float(input('Qual a altura da parede? '))

n2 = float(input('\nQual o comprimento da parede? '))
print('\nA área da parede é {}m² \n\nVocê irá precisa de {:.2f} Litros de tinta para cobrir.\n'.format(n1*n2, (n1*n2)/2))
