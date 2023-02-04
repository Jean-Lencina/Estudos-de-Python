from math import sin, cos, tan, radians
an = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O Ângulo de {} tem o SENO de {:.2f}\nO COSSENO de {:.2f}\nA TANGENTE de {:.2f}'.format(an, seno, cos, tan))
