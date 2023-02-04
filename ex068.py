from random import randint
cont = 0
print('=-' *30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' *30)
while True:
    comp = randint(0,10)
    jogador = int(input('Diga um valor: '))
    jogada = ' '
    print('-' *30)
    soma = comp + jogador
    while jogada not in 'PI':
        jogada = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if jogada == 'P' and soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador {comp}. Total de {soma} DEU PAR')
        print('=-' * 20)
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 20)
        cont += 1
    elif jogada == 'I' and soma % 2 == 1:
        print(f'Você jogou {jogador} e o computador {comp}. Total de {soma} DEU ÍMPAR')
        print('=-' * 20)
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 20)
        cont += 1
    else: 
        print('Você PERDEU!')
        break
print('-=' * 30)        
print(f'GAME OVER! Você venceu {cont} vezes.')
