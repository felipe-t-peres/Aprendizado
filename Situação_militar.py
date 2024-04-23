from datetime import date
print('-=-' * 20)
n1 = int(input('Em que ano você nasceu? '))
print('-=-' * 20)
n2 = date.today().year
n3 = n2 - n1
print('Neste ano de {} você está com {} anos e sua situação militar é a seguinte: '.format(n2, n3))
print('-=-' * 20)
if n3 < 17:
    print('Com {} anos você ainda não precisa se preocupar com o alistamento Militar.'.format(n3))
    print('\nFaltam {} anos para seu alistamento.'.format(18 - n3))
elif n3 >= 17 and n3 <= 18:
    print('Com esta idade {} anos, você deve procurar uma junta militar mais próxima de você!'.format(n3))
elif n3 > 18 and n3 <= 20:
    print('Seu prazo de alistamento já passou em {} anos, como está sua situação?'.format(n3 - 18))
elif n3 > 21:
    print('Toma vergonha nessa cara, seu alistamento já expirou há muito tempo')
print('-=-' * 20)
