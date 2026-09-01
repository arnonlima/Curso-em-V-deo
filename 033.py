print('Quem é maior')

a=float(input('Diga um numero: '))
b=float(input('Diga um numero: '))
c=float(input('Diga um numero: '))
if a > b and a > c:
    print('O primeiro valor é maior')
elif b > a and a > c:
    print('O segundo valor é maior')
else:
    print('O terceiro valor é maior')
 