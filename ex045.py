from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
if jogador == 0 or jogador == 1 or jogador == 2:
    print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:  # computador jogou pedra
    if jogador == 0:  # jogador jogou pedra
        print('EMPATE')
    elif jogador == 1:  # jogador jogou papel
        print('Jogador Ganhou')
    elif jogador == 2:  # jogador jogou tesoura
        print('Computador ganhou')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:  # computador jogou papel
    if jogador == 0:   # jogador jogou pedra
        print('Computador ganhou')
    elif jogador == 1:  # jogador jogou papel
        print('EMPATE')
    elif jogador == 2:  # jogador jogou tesoura
        print('Jogador ganhou')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:  # computador jogou tesoura
    if jogador == 0:  # jogador jogou pedra
        print('Jogador ganhou')
    elif jogador == 1:  #jogador jogou papel
        print('Computador ganhou')
    elif jogador == 2:  #jogador jogou tesoura
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
