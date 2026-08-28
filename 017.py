#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

cat_oposto=float(input('Diga o cateto oposto: '))
cat_adj=float(input('Diga o cateto adjacente: '))
hip=(cat_oposto**2+cat_adj**2)**0.5
print(f'A hipotenusa do triangulo é {hip:.2f}')
    
import math

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f"A hipotenusa mede {hipotenusa:.2f}")