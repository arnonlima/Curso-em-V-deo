print('Limite de velocidade')
while True:
 n=int(input('Diga a velocidade: 0 para sair: '))
 if n ==0:
  break
 elif n>80:
    excesso=n-80
    multa= excesso*7
    print(f'Carro ultrapassou o limite de velocidade, irá pagar uma multa de {multa:.2f} reais.')
 else:
     print(' Carro na velocidade permitida')