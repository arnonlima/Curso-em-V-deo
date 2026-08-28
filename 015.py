#Escreva um programa que pergunte a quantidade de Km percorridos por um carro 
# alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R0,15 por Km rodado.

n1=float(input('Diga quantos km o carro percorreu: '))
n2=int(input('Diga quantos dias o carro foi alugado: '))
kmdia=n1*0.15
dia= n2*60
aluguel= (kmdia)+(dia)
print(f'O custo do aluguel carro foi R$ {aluguel:.2f} reais')

