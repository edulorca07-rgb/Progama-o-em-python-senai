numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
    

idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("Você ainda não pode votar.")
elif 18 <= idade <= 70:
    print("O voto é obrigatório.")
else:
    print("O voto é opcional")

numero = 15


if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")


lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))


if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

    if lado1 == lado2 == lado3:
        print("O triângulo é Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é Isósceles.")
    else:
        print("O triângulo é Escaleno.")


def verificar_multiplo_v1(numero):
    if numero % 5 == 0 and numero % 7 == 0:
        return f"O número {numero} é múltiplo de 5 e 7."
    else:
        return f"O número {numero} NÃO é múltiplo de 5 e 7."
   
   
   
numero = 15

if numero > 0 and numero > 10:
    print("O número é positivo e maior que 10.")
else:
    print("O número não atende aos requisitos.")


numero = int(input("Digite um número: "))

if numero % 3 == 0 or numero % 5 == 0:
    print(f"O número {numero} é divisível por 3 ou por 5.")
else:
    print(f"O número {numero} NÃO é divisível por 3 nem por 5.")
    