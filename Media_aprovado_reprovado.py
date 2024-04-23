print('-=-' * 20)
n1 = float(input('Nota da primeira avaliação: '))
n2 = float(input('Nota da segunda avaliação: '))
n3 = (n1 + n2)/2
print('-=-' * 20)
if n3 < 5.0:
    print('Sua média foi de {:.1f}, desculpe, mas você está reprovado(a).'.format(n3))
elif n3 >= 5.1 and n3 <= 6.9:
    print('Sua media foi de {:.1f} e você está em recuperação, confira com seu professor a nova data de prova.'.format(n3))
elif n3 >= 7.0:
    print('Parabéns, sua média ficou {:.1f} e você está de férias.'.format(n3))
print('-=-' * 20)