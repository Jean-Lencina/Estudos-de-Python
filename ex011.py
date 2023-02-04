larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg*alt
print('A sua parede tem dimensão de {} x {} e sua área é de {:.2f}m².'. format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {:.1f}l de tinta.'. format(tinta))
