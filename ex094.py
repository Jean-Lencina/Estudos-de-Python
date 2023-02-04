dados = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    dados.append(pessoa.copy())
    while True:
        cont = str(input('Quer continuar? ')).upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if cont == 'N':
        break
print('-' * 30)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas')
media = soma / len(dados)
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista de pessoas que estão acima da média: ' )
for p in dados:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')