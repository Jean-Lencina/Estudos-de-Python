from ast import Break

num = []
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor Duplicado! Não vou adicionar...')
    while True:
        cont = str(input('Quer continuar? [S/n] ' ))
        if cont in 'Ss':
            break
        if cont in 'Nn':
            break            
        else:
            print('Opção inválida. Tente novamente...')
    if cont in 'Nn':
        break
print(f'Você adicionou os valores: {sorted(num)}')
