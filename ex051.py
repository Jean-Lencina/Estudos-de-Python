print('=' * 40)
print(' ' * 10, '10 TERMOS DE UMA PA')
print('=' * 40)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
print('=' * 60)
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='→ ')
print('ACABOU')
print('=' * 60)
