print('Par ou impar: 0 para sair')
while True:
 n=int(input('Diga um número: '))
 if n==0:
     break
 elif n%2==0:
     print(' O numero é par')
 else:
     print('O numero é impar')
 