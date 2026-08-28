#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
# mostre quantos dólares ela pode comprar.

n1=float(input('Diga quanto em reais você tem: '))
n2=float(input('Diga a cotação do dolar: '))
conversao=n1/n2
print(f'Você pode comprar {conversao:.2f} dolares')