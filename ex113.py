def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[31mERRO! Digite um número válido\033[m')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            nreal = float(input(msg))
        except:
            print('\033[31mERRO! Digite um número válido\033[m')
        else:
            return nreal


n1 = leiaint('Digite um numero inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'O valor inteiro foi {n1} e o real foi {n2}')
