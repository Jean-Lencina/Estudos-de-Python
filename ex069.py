print('-' * 30)
print('     CADASTRE UMA PESSOA')
print('-' * 30)
contid = contsm = contsf = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        contid += 1
    if sexo == 'M':
        contsm += 1   
    if sexo == 'F' and idade < 20:
        contsf += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('FIM DO PROGRAMA')
print(f'Total de pessoas com mais de 18 anos: {contid}')
print(f'Ao todo temos {contsm} homens cadastrados') 
print(f'E temos {contsf} mulheres com menos de 20 anos')
