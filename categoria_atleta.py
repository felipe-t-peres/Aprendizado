from datetime import date
ano = date.today().year
print('-=-' * 20)
n1 = int(input('Ano de nascimento do atleta: '))
n2 = ano - n1
print('-=-' * 20)
if n2 <= 9:
    print('O atleta tem {} anos, sua categoria é: MIRIM'.format(n2))
elif n2 > 9 and n2 <= 14:
    print('O atleta tem {} anos, sua categoria é: INFANTIL'.format(n2))
elif n2 > 14 and n2 <= 19:
    print('O atleta tem {} anos, sua categoria é: JUNIOR'.format(n2))
elif n2 > 19 and n2 <= 20:
    print('O atleta tem {} anos, sua categoria é: SÊNIOR'.format(n2))
else:
    print('O atleta tem {} anos, sua categoria é: MASTER'.format(n2))
print('-=-' * 20)