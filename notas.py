nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
nota3 = float(input('Nota 3:'))

media = (nota1 + nota2 + nota3)/3

passar = media >=7
recuperacao = media >= 5 and media < 7
reprovado = media < 5

print('aprovado - situação:', passar)
print('Recuperação - situação:', recuperacao)
print('Reprovado - situação', reprovado)

