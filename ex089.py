ficha = list()
print('-' * 30)
print(f'{"REGISTRADOR DE NOTAS":^30}')
print('-' * 30)
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    while True:
        resp = str(input('Você que continuar? [S/N]'))
        if resp in 'Nn':
            break
        if resp in 'Ss':
            break
        else:
            print('Você digitou um comando inválido. Tente novamente...')
    if resp in 'Nn':
        break
print('-' * 30)
print(f'{"BOLETIM":^30}')
print('-' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    else:
        print('Você digitou uma opção inválida. Tente novamente...')
print('<<< VOLTE SEMPRE >>>')
