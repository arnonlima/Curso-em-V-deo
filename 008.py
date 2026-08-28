#: Escreva um programa que leia um valor em metros e o 
# exiba convertido em centímetros e milímetros.

n1=float(input('Digite um valor em metros: '))
centimetro=n1*100
milimetro=n1*1000
print('O valor em {} centimetros e em {} milimetros'.format(centimetro,milimetro))
