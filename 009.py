#Faça um programa que leia um número Inteiro qualquer e 
# mostre na tela a sua tabuada.

n1=int(input('Diga um numero: '))
tabuada=[n1*i for i in range(1,11)]
print(f'A tabuada do {n1} é:{tabuada} ')
