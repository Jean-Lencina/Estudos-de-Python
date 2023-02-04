lista = list()
par = list()
impar= list()
while True:
    lista.append(int(input('Digite um número: ')))
    while True:    
        cont = str(input('Quer continuar? [S/n] ' ))
        if cont in 'Ss':
            break
        elif cont in 'Nn':
            break            
        else:
            print('Opção inválida. Tente novamente...')
    if cont in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    if v % 2 == 1:
        impar.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
