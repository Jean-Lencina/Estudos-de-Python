print('# Vamos calcular o valor da sua passagem #')
distancia = float(input('Digite a distância da sua viagem: '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('Sua passagem vai custar R${:.2f}'.format(preço))
