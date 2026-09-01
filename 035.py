print('====MENU====')
print('[1] Verificar Triangulo')
print('[2] Sair')
opcao=int(input('Escolha uma opcao: '))
if opcao == 1:
 print('Triangulos')
 a=float(input('Diga um comprimentos: '))
 b=float(input('Diga um comprimentos: '))
 c=float(input('Diga um comprimentos: '))
 if a+b>c and a+c>b and b+c>a:
    print('Os comprimentos formam um triângulo')
 
 else:
    print('Não podem formar um triângulo')
elif opcao ==2:
    print('Saiu do programa')
    