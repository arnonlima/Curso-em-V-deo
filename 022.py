#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas
#- O nome com todas as letras minúsculas
#- Quantas letras ao todo (sem considerar espaços)
#- Quantas letras tem o primeiro nome

n=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {n.upper()}')
print(f'Seu nome em minúsculas é {n.lower()}')
print(f'Seu nome tem ao todo {len(n) - n.count(" ")} letras')
print(f'Seu primeiro nome tem {len(n.split()[0])} letras')
print(f'Seu nome em título é {n.title()}')
print(f'Seu primeiro nome é {n.split()[0]}')
