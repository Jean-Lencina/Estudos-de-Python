menor = quant = total = totmil = 0
barato = ''
while True:
    prod = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    quant += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if quant == 1 or preço < menor:
        maior = menor = preço
        barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {totmil} produtos custando mais de de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
