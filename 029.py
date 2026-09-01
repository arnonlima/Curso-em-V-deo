#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#  mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por 
# cada Km acima do limite.


print('Limite de velocidade')
while True:
 n=int(input('Diga a velocidade:  ou 0 para sair: '))
 if n ==0:
  break
 elif n>80:
    excesso=n-80
    multa= excesso*7
    print(f'Carro ultrapassou o limite de velocidade, irá pagar uma multa de {multa:.2f} reais.')
 else:
     print(' Carro na velocidade permitida')