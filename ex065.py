res = 'S'
quant = soma = media = maior = menor = 0
while res in 'Ss:':
    núm = int(input('Digite um número:'))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    res = str(input('Quer continuar?[S/N]')).upper().strip()
media = soma / quant
print(f'Você digitou {quant} valores e a média foi {media}')
print(f'O maior número digitado foi {maior} e o menor foi o {menor}')
