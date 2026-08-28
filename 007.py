#Desenvolva um programa que leia as duas notas de um aluno,
#  calcule e mostre a sua média.

n1=float(input('Diga a sua primeira nota: '))
n2=float(input('Diga a sua segunda nota: '))
n3=float(input('Diga a sua terceira nota: '))
media=(n1+n2+n3)/3
print('A sua média é {:.2f}.'.format(media))