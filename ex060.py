'''Calculando fatorial com a estrutura WHILE:'''
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

'''Calculando Fatorial com a estrutura FOR:'''
#n = int(input('Digite um número para calcular seu Fatorial: '))
#f = 1
#print('Calculando {}! = '.format(n), end='')
#for c in range(n, 0, -1):
#    print(c, end='')
#    print(' x ' if c > 1 else ' = ', end='')
#    f *= c
#print('{}'.format(f))