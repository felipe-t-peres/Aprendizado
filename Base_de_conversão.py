# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher 
# qual será a "base de conversão":
# - 1 para binário 
# - 2 para octal 
# - 3 para hexadecimal

n1 = int(input('Digite um número inteiro: '))
print('Escolha uma das opções abaixo: \n[ 1 ] para BINÁRIO \n[ 2 ] para OCTAL \n[ 3 ] para HEXADECIMAL')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n1, bin(n1)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n1, oct(n1)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção inválida...')
    