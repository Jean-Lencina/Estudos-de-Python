valor = list()
while True:
    valor.append(int(input('Digite um número: ')))
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
print(f'Você digitou {len(valor)} elementos.')
valor.sort(reverse=True)
print(f'Os valores em ordem decrescente foram {valor}')
if 5 in valor:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista.')