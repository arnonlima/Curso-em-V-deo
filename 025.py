#Crie um programa que leia o nome de uma pessoa e 
# diga se ela tem "SILVA" no nome.

n=str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem \'Silva\'?')
print('SILVA' in n.upper()) 
print('Seu nome tem Lima?')
print('LIMA' in n.upper())
