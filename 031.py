#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem,ate 200km é 0,50 reais por km e cobrando Ré0,45 parta 
# viagens mais longas.

distancia = float(input('Digite a distância da viagem em Km: '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da passagem é de R${preco:.2f}')
