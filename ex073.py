times = ('Cruzeiro', 'Grêmio', 'Bahia', 'Vasco', 
        'Sport', 'Sampaio Corrêa', 'Criciúma', 
        'Ituano', 'Londrina', 'Guarani', 'CRB', 
        'Ponte Preta', 'Vila Nova', 'Tombense', 
        'Novorizontino', 'Chapecoense', 'CSA', 
        'Operário-PR', 'Brusque', 'Náutico')
print(f'Lista de times: {times}')
print('-=' * 63)
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('-=' * 63)
print(f'os ultimos colocados são: {times[-4:]}')
print('-=' * 63)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-=' * 63)
print(f'O chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
