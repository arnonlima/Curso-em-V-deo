#Faça um programa que leia um ângulo qualquer e 
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo=float(input('Digite um angulo: '))
r=math.radians(angulo)
print(f'sen={math.sin(r):.2f}')
print(f'cos={math.cos(r):.2f}')
print(f'tan={math.tan(r):.2f}')
