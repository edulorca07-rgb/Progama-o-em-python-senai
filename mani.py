import random


numero_aleatorio = random.randrange(5, 10)

print(numero_aleatorio)

import random


numero_aleatorio = random.randrange(10, 31)

print(numero_aleatorio)

import time


for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("Fogo!")


numero = int(input("Digite um número inteiro positivo: "))


if numero > 0:
    soma_pares = 0
    
    for i in range(2, numero + 1, 2):
        soma_pares += i
        
    print(f"A soma de todos os números pares de 2 até {numero} é: {soma_pares}")
else:
    print("digite um número inteiro maior que zero.")

    numero = int(input("Digite um número inteiro: "))
print(f"Tabuada do {numero}:")

for i in range(1, 11):
    print(f"{numero} X {i} = {numero * i}")

for i in range(99, 0, -2):
    print(i)
