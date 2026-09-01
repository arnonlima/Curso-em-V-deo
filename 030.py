#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print('Par ou impar: 0 para sair')
while True:
 n=int(input('Diga um número: '))
 if n==0:
     break
 elif n%2==0: # Verifica se o número é par
     print(' O numero é par')
 else:
     print('O numero é impar')
 