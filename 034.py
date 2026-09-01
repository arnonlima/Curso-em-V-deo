#: Escreva um programa que pergunte o salário de um funcionário e 
# calcule o valor do seu aumento. Para salários superiores a R$1250,00, 
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print("Salarios")
while True:
     n=float(input('Diga o salario: ou 0 para sair: '))
     if n > 1250:
        x=n*1.10
        print(f'O novo salario do funcionario é {x:.2f} reais')
     elif n==0:
        break
     else:
        y=n*1.15
        print(f'O novo salario do funcionario é {y:.2f} reais')
        
 

