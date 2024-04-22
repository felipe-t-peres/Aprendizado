#Minha solução
n1= float(input('\nQual a distância a ser percorrida: '))
if n1<= 200:
    print('\nA viagem vai custar R${:.2f}\n'.format(n1*0.50))
else:
    print('\nA viagem vai custar R${:.2f}\n'.format(n1*0.45))

#SOlução Professor

distância = float(input('\nQual é a distância da sua viagem? '))
print('\nVocê esta prestes a começar uma viagem de {}Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('\nE o preço da sua passagem será de R${:.2f}\n'.format(preço))
