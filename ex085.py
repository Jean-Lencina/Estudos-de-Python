num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
if len(num[0]) == 0:
    print('Você não digitou valor par.')
else:
    print(f'Os números pares digitados foram: {num[0]}')
if len(num[1]) == 0:
    print('Você não digitou valor ímpar.')
else:
    print(f'Os números ímpares digitados foram: {num[1]}')
