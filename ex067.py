while True:
    print('-' *30)
    núm = int(input('Quer ver a tabuada de qual valor? '))
    print('-' *30)
    if núm < 0:
        break
    for c in range(1, 11):
        print(f'{núm} x {c} = {núm * c}')
print('PROGRAMA TABUADA ENCERRADO! Volte sempre!')