#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#  em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase=str(input('Digite uma frase: ')).strip()
print(f'A letra "A" aparece {frase.upper().count("A")} vezes.')
print(f'A primeira vez que ela aparece é na posição {frase.upper().find("A")}.')
print(f'A última vez que ela aparece é na posição {frase.upper().rfind("A") - frase.count("A") }.')
print('A frase tem {} letras'. format(len(frase) - frase.count(' ')))

#Mesma linha de raciocínio, mas com a letra R.

n=str(input('Digite uma frase: ')).strip()
print(f'A letra "R" aparece {n.upper().count("R")} vezes.') 
print(f'A primeira vez que ela aparece é na posição {n.upper().find("R")}.')
print(f'A última vez que ela aparece é na posição {n.upper().rfind("R") - n.count("R") }.')
print('A frase tem {} letras'. format(len(n) - n.count(' ')))
