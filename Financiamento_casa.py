# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. 
# O programa vai perguntar: 
#           - o valor da casa, 
#           - o salário do comprador, 
#           - em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do Salário ou então o emprestimo será negado.

print('-=-' * 20)
vlcasa = float(input('Qual o valor da casa? R$'))
print('-=-' * 20)
slcomp = float(input('Qual seu salário? R$'))
print('-=-' * 20)
anos = int(input('Em quantos anos deseja pagar? '))
print('-=-' * 20)
qtdparcelas = anos * 12
prest = vlcasa/qtdparcelas
limite30 = slcomp * 0.3
if prest <= limite30:
    print('Seu empréstimo foi aprovado.')
    print('Você pagará {:.0f} parcelas mensais de R${:.2f}'.format(qtdparcelas, prest))
else:
    print('Seu emprestimo foi negado!')
    print('O valor da prestação ficou em R${:.2f} e você pode pagar até R${:.2f} por mês!'.format(prest, limite30))
print('-=-' * 20)
