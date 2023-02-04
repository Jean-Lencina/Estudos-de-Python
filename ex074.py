from random import randint

sort = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Eu sorteei os números: {sort}')
print(f'O maior valor foi {max(sort)}')
print(f'O menor valor foi {min(sort)}')
if max(sort) % 2 == 0:
    print('PAR')
else:
    print('Ímpar')
