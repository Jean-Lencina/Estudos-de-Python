num = int(input('Digite um número para ver sua tabuada:'))
print('-' * 20)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print('-' * 20)