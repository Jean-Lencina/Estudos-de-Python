casa = float(input('Valor da casa: R$ '))
salario = float(input('Sálario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * (30/100)
if prestacao <= minimo:
    print('Financiamento negado')
else:
    print('Financiamento aprovado')

