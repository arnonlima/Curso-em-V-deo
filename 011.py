#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

n1 = float(input('Diga quantos metros de largura: '))
n2 = float(input('Diga quantos metros de altura: '))
area = n1 * n2
tinta = area / 2
print(f'Você vai precisar de {tinta:.2f} latas de tintas')