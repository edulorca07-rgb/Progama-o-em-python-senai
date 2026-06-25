contador = 0

while contador <= 1000:
    print(contador)
    contador += 1


    nomes = []
contador = 0


while contador < 10:
    nome = input(f"Digite o nome da {contador + 1}ª pessoa: ")
    nomes.append(nome)
    contador += 1


print("\n--- Pessoas Cadastradas ---")
for n in range (10):
    nome = input ('nome:')
    print(nome)