print('-=-' * 20)
print('Digite o valor de cada reta: ')
print('-=-' * 20)
r1 = float(input('r1: '))
r2 = float(input('r2: '))
r3 = float(input('r3: '))
print('-=-' * 20)

if r1 < r2+r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os valores podem formar um triangulo!')
    if r1 == r2 == r3:
        print('E este triangulo é chamado de EQUILÁTERO.')
    if r1 == r2 and r1 != r3 and r2 !=r3 or r1 != r2 and r1 == r3 and r2 !=r3 or r1 != r2 and r1 != r3 and r2 ==r3:
        print('E este triangulo é chamado de ISÓSCELES.')
    if r1 != r2 and r1 != r3 and r2 !=r3:
        print('E este triangulo é chamado de ESCALENO.')
else:
    print('Não pode formar um triangulo!')
print('-=-' * 20)