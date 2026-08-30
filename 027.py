#Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

nome=str(input('Diga o seu nome: ')).strip()# remove espaços em branco no início e no final da string
n=nome.split()# Divide o nome em partes separadas por espaços
print(f'O primeiro nome é {n[0]}.')
print(f'O ultimo nome é {n[-1]}.')#-1 representa o último elemento da lista