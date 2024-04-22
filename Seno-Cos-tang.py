'''
import math
n1= float(input('Qual o valor do angulo: '))
c = math.cos(math.radians(n1))
s = math.sin(math.radians(n1))
t = math.tan(math.radians(n1))
print('Para o angulo de {} graus temos:'.format(n1))
print('{:.2f} de coseno'.format(c))
print('{:.2f} de seno'.format(s))
print('{:.2f} de tangente'.format(t))

'''

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tang = tan(radians(an))
print('O angulo de {} tem os seguintes valores: '.format(an))
print('Seno: {:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(cosseno))
print('Tangente: {:.2f}'.format(tang))
