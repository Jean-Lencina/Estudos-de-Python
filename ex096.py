def Área(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é {a}')


print('-' * 20)
print(f'{"Controle de Terrenos":^20}')
print('-' * 20)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
Área(l, c)