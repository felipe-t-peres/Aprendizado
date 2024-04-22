'''crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome'''
nome= str(input('Diga o nome de uma pessoa: ')).strip()
sva=nome.lower()
print('O nome digitado contem Silva: {}'.format('silva' in sva))