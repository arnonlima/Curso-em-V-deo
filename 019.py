#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele,lendo o nome dos alunos e 
# escrevendo na tela o nome do escolhido.

import random
n1=input('Diga o nome do primeiro aluno: ')
n2=input('Diga o nome do segundo aluno: ')
n3=input('Diga o nome do terceiro aluno: ')
n4=input('Diga o nome do quarto aluno: ')
sorteio=random.choice([n1,n2,n3,n4])
print(f'O aluno escolhido foi {sorteio}')