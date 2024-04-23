''' Minha solução '''
import random
n1 = int(input('\nPensei em um numero e está entre 0 e 5 tente advinhar qual foi, diga ai do lado: '))
lista = ['0', '1', '2', '3', '4', '5']
sorte = random.choice(lista)

print('\nO numero que eu escolhi foi: {}\n'.format(sorte))
if n1==sorte:
    print('\nVocê acertou, parabéns!!\n')
else:
    print('\nNão foi dessa vez, continue tentando!!\n')

# Solução professor

from random import randint
from time import sleep
computador = randint(0 , 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
