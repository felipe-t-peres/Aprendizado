n1= float(input('\nQual o valor do seu salário? R$'))
if n1<=1250:
    print('\nO seu aumento será de 15% e o montante final ficará em R${:.2f}\n'.format((n1*0.15)+n1))
else:
    print('\nO seu aumento será de 10% e o montante final ficará em R${:.2f}\n'.format((n1*0.1)+n1))