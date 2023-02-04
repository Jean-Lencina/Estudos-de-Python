from time import sleep

primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>>>> Qual é a sua opção? '))
    print('=-=' * 10)
    if opção == 1:
        soma = primeiro + segundo
        print('A soma entre {} + {} é {}'.format(primeiro, segundo, soma))
    elif opção == 2:
        produto = primeiro * segundo
        print('O resultado de {} x {} é {}'.format(primeiro, segundo, produto))
    elif opção == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print('Entre {} e {} o maior valor é {}'.format(primeiro, segundo, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
