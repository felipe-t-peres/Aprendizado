from datetime import date
n1=int(input('\nQual o ano de sua curiosidade? '))
if n1 == 0:
    n1 = date.today().year
if n1%4 == 0 and n1 % 100 != 0 or n1 % 400 == 0:
    print('\nÉ um ano Bissexto!\n')
else:
    print('\nNão é bissexto!\n')
