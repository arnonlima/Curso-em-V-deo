#Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.

n=int(input('Digite um número de 0 a 9999: '))
print(f'Unidade: {n // 1 % 10}')
print(f'Dezena: {n // 10 % 10}')
print(f'Centena: {n // 100 % 10}')
print(f'Milhar: {n // 1000 % 10}')

#Outra maneira de fazer é usando o format, que é mais elegante e fácil de ler:
print('Unidade: {}'.format(n//1%10))
print('Dezena: {}'.format(n//10%10))
print('Centena: {}'.format(n//100%10))
print('Milhar: {}'.format(n//1000%10))
