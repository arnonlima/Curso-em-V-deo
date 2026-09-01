import random
numero_secreto=random.randint(1,5)
print('Jogo da adivinhacao')
while True:
       n=int(input('Escolha um número de 1 a 5:'))
       if n==numero_secreto:
           print('Parabens, você ganhou!!!')
           break
       elif n>=numero_secreto:
           print('Tente um numero menor')
       else:
           print('Tentw um numero maior')

