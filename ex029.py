vel = float(input('Qual a velocidade atual do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80 Km/h.')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
