from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informado foi {maior}')
    print()


maior(2, 11, 6, 4, 10, 5)
maior(2, 13, 5 , 20, 3)
maior(0, 5, 9, 12)
maior(15, 3, 1)
maior()
