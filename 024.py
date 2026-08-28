#Crie um programa que leia o nome de uma cidade diga
#  se ela começa ou não com o nome "SANTO"

cidade=str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')


#Mesma linha de raciocínio, mas se inicia com o nome de São.

cidade=str(input('Diga um nome de uma cidade: ')).strip()
print(cidade[:3].upper()=='SÃO')

#Mesma linha de raciocínio, mas se termina com grande.

cidade=str(input('Diga o nome de uma cidade: ')).strip()
print(cidade[-6:].upper()=='GRANDE')