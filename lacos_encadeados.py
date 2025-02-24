#Princípios de encadeamento de laços de repetição:

for cont_ex in range (1,6):
    print(f'\nRodada: {cont_ex}')
    for cont_int in range (5,-1,-1):
        print(f'\nValor: {cont_int}')
print('\nFinal dos Laços!')


import random

for a in range (0,6):
    print(f'\nConjunto: {a}\n')
    for b in range (5):
        numero = random.randint(0,1000)
        print(f'Valor: {numero}')

#Explicação:

#importamos 'random' que é um módulo 'built-in' de Python

# Para todo 'a' entre 0 e 6
# Printar uma string 'Conjunto' de 'a' que
# Encadeia 'b' que gera 5 numeros aleatórios entre 0 e 1000 cada conjunto.