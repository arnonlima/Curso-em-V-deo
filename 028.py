#Escreva um programa que faça o computador "pensar" em um número inteiro 
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o 
# número escolhido pelo computador. O programa deverá escrever na tela 
# se o usuário venceu ou perdeu.

import random
numero_secreto=random.randint(1,5) #random.randint() gera um número aleatório entre 1 e 5
print('Jogo da adivinhacao')
while True:
       n=int(input('Escolha um número de 1 a 5:'))
       if n==numero_secreto:
           print('Parabens, você ganhou!!!')
           break
       elif n>=numero_secreto:
           print('Tente um numero menor')
       else:
           print('Tente um numero maior')

