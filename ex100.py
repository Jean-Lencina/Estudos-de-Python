from random import randint
from time import sleep

def sorteie(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos pares de {lista}, temos {soma} ', end='')
    print('PRONTO!')
num = list()
sorteie(num)
somapar(num)
