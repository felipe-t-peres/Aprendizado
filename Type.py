n= input('Digite alguma coisa: ')
print('Isto que você digitou, {}, é... '.format(n))
print("...um numero? {} ".format(n.isnumeric()))
print("...uma letra? {} ".format(n.isalpha()))
print("...algo que foi escrito em letras minusculas? {} ".format(n.islower()))
print("...um numero e letras? {} ".format(n.isalnum()))
print('O tipo primitivo do que foi digitado é: {}'.format(type(n)))
print('Só tem espaços? ', n.isspace())

# n= input('Digite alguma coisa: ')
# print('Isto que você digitou, {}, é... '.format(n))
# print("...um numero? ",n.isnumeric())
# print("...uma letra? ",n.isalpha())
# print("...algo que foi escrito em letras minusculas? ",n.islower())
# print("...um numero e letras? ",n.isalnum())
# print('O tipo primitivo do que foi digitado é: ',type(n))
# print('Só tem espaços? ', n.isspace())
