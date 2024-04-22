km = float(input('Quantos Km foram rodados: '))
di = int(input('Por quantos dias ele foi alugado: '))
vc = 60 * di
vkm = km * 0.15
print('O valor total do carro que rodou {} Km, alugado por {:.0f} dias, foi de R${:.2f}'.format(km, di, vc + vkm))
