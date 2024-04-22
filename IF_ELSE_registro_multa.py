n1 = float(input('\nQual a velocidade registrada do automovel? '))
n2 = (n1 - 80)*7
if n1 > 80:
    print('\nQue feio, você foi multado...\n\nPassou {:.0f}Km acima do limite de velocidade\n \nA multa vai custar R${:.2f}\n'.format(n1-80, n2))
else:
    print('\nContinue assim, sendo um bom motorista!\n')
