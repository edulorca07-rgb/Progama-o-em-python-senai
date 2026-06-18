minha_lista = [1, 2, 3, 4, 5]
lista_vazia = []

primeiro_elemento = minha_lista[0]
print(primeiro_elemento)  # Isso imprimirá 1


minha_lista.append(6)
print(minha_lista)  # Agora a lista conterá [1, 2, 3, 4, 5, 6]


comprimento = len(minha_lista)
print(comprimento)  # Isso imprimirá 4 (após a remoção de elementos)



for elemento in minha_lista:
    print(elemento)



lista_mista = [1, "Python", 3.14, True]



Em python listas:
0   1 2  3  4  5  6 7 8 acessando 
[12,3,6,89,45,78,1,2,3]
-9 -8 -7 -6 -5 -4 -3-2-1 acessando também


Exemplo mercado: 

produtos =  ['arroz - 0','bebida - 1','coca - 2']
print('Produtos disponiveis', produtos)
valores =  [10.2,20.0,30.00]
print('Valores R$', valores)

meu_carrinho = []
meu_total = []
escolha1  =  int(input('Digite o id 0-1-2'))
escolha2  =  int(input('Digite o id 0-1-2'))
escolha3  =  int(input('Digite o id 0-1-2'))
escolha4  =  int(input('Digite o id 0-1-2'))

meu_carrinho.append(produtos[escolha1])
meu_total.append(valores[escolha1])
meu_carrinho.append(produtos[escolha2])
meu_total.append(valores[escolha2])
meu_carrinho.append(produtos[escolha3])
meu_total.append(valores[escolha3])
meu_carrinho.append(produtos[escolha4])
meu_total.append(valores[escolha4])

print('Seus produtos são:', meu_carrinho)
print('***' * 21)
total =  sum(meu_total)
print('R$', total)

------------------------------------

produtos =  ['arroz - 0','bebida - 1','coca - 2']
print('Produtos disponiveis', produtos)
valores =  [10.2,20.0,30.00]
print('Valores R$', valores)

meu_carrinho = []
meu_total = []
escolha1,escolha2, escolha3,escolha4  =  int(input('Digite o id 0-1-2')), int(input('Digite o id 0-1-2')),  int(input('Digite o id 0-1-2')),  int(input('Digite o id 0-1-2'))

meu_carrinho.extend([produtos[escolha1], produtos[escolha2], produtos[escolha3],  produtos[escolha4] ])
meu_total.extend([valores[escolha1], valores[escolha2], valores[escolha3],  valores[escolha4]])


print('Seus produtos são:', meu_carrinho)
print('***' * 21)
total =  sum(meu_total)
print('R$', total)



listas:

# append() - adiciona um elemento à lista
lista = [1, 2, 3]
lista.append(4)
print(lista)  # Saída: [1, 2, 3, 4]

# sum() - soma todos os elementos da lista
soma = sum(lista)
print(soma)  # Saída: 10

# max() - retorna o valor máximo da lista
maximo = max(lista)
print(maximo)  # Saída: 4

# clear() - limpa todos os elementos da lista
lista.clear()
print(lista)  # Saída: []

# copy() - faz uma cópia da lista
lista = [1, 2, 3]
copia = lista.copy()
print(copia)  # Saída: [1, 2, 3]

# extend() - adiciona os elementos de uma lista à outra lista
lista.extend([4, 5, 6])
print(lista)  # Saída: [1, 2, 3, 4, 5, 6]

# count() - conta a quantidade de ocorrências de um elemento na lista
quantidade = lista.count(4)
print(quantidade)  # Saída: 1

# index() - retorna o índice do primeiro elemento encontrado na lista
indice = lista.index(3)
print(indice)  # Saída: 2

# insert() - insere um elemento em uma posição específica da lista
lista.insert(1, 7)
print(lista)  # Saída: [1, 7, 2, 3, 4, 5, 6]

# pop() - remove e retorna o último elemento da lista
elemento_removido = lista.pop()
print(elemento_removido)  # Saída: 6
print(lista)  # Saída: [1, 7, 2, 3, 4, 5]

# remove() - remove a primeira ocorrência de um elemento da lista
lista.remove(2)
print(lista)  # Saída: [1, 7, 3, 4, 5]

# sort() - ordena os elementos da lista (por padrão, em ordem crescente)
lista.sort()
print(lista)  # Saída: [1, 3, 4, 5, 7]

# Ordenação em ordem decrescente
lista.sort(reverse=True)
print(lista)  # Saída: [7, 5, 4, 3, 1]






lista =  [1,6,6,10,89,4]
print(len(lista))
# verificar o tamanho da minha lista
# --------------------------------
#adiciono um valor dentro da lista 
lista.append(10)
# acessar um indice e atribuir um novo valor ao indice
lista[0] = 2
print(lista)

# --------------------------------

# remover o valor da lista pelo indice(index)
del lista[0] # vai re
print(lista)
# vai remover pelo valor(value)
lista.remove(89)
print(lista)

# -------------------------------


#  Lista em python exemplos:  

lista  =  [1,2,3,6]

# append(1  dado) extended([varios]) +=(varios) insert(indice,dado) # adicionar

# del lista[indice] remove(valor) pop(indice) pop() deletar o ultimo #deletar

# len() sum() min() max() copy() clear() # verificar
tamanho = len(lista)
print(tamanho)

# sum - somar
lista  =  [1,2,3,6]
somar = sum(lista)
print(somar)

menor  =  min(lista)
print(menor)

maior  =  max(lista)
print(maior)

copia = lista.copy()
print(copia)

lista.clear()
print(lista)


# inserir
lista  =  [] # LISTA VAZIA*** 

# append  -  inserir um dado
lista.append(10)

# extend  -  varios dados de uma vez
lista.extend([10,30,3010,30,30])

# (+=) -  inseri varios dados tb
lista +=(10,30,30,10,30,30)

# insert -  inserir na posição que você quiser
lista.insert(0,1500)

print(lista)

-----

# remover

# remove() remove por valor não por indice
lista.remove(1500)

# del - remove por indice
del lista[0]

# pop() -  remove ultimo valor
lista.pop()

# pop(com indice) -  remove o indice que vc quiser
lista.pop(2)
print(lista)


------------
# verificar algo
# tamanho  -  len()
print(len(lista))

# somar a numeros das listas
print(sum(lista))

# max() maior numero da lista
maior = max(lista)
print(maior)

# min() menor numero da lista
menor =  min(lista)
print(menor)

# count() quantidade de algum dado especifico dentro da lista
print(lista.count(30))

# sort() orgdanizar do menor para o maior
lista.sort(reverse = True )# maior para o menor 
lista.sort() # menor para maior
print(lista)

# copy() copia a lista 
copia  =  lista.copy()
print(copia)


# clear() limpa a lista
lista.clear()
print(lista)


----


# E-commerce

carrinho = []
meu_total   = []

# listas 
lista_produtos = ['','hd','ssd','iphone 17', 'pc dell']
valores_produtos = [0,500.55,20.5,7000.0,8000.99]
print(f'''
{lista_produtos[1]}  -  R$ {valores_produtos[1]}
{lista_produtos[2]}  -  R$ {valores_produtos[2]}
{lista_produtos[3]}  -  R$ {valores_produtos[3]}
{lista_produtos[4]}  -  R$ {valores_produtos[4]}
''')


# variáveis que vão escolher o produto da lista
produto_1 = int(input('ID do produto: '))
produto_2 = int(input('ID do produto: '))
produto_3 = int(input('ID do produto: '))

carrinho.append(lista_produtos[produto_1])
print('Você inseriu no seu carrinho - ', carrinho)
meu_total.append(valores_produtos[produto_1])
print('R$', sum(meu_total))

carrinho.append(lista_produtos[produto_2])
print('Você inseriu no seu carrinho - ', carrinho)
meu_total.append(valores_produtos[produto_2])
print('R$', sum(meu_total))

carrinho.append(lista_produtos[produto_3])
print('Você inseriu no seu carrinho - ', carrinho)
meu_total.append(valores_produtos[produto_3])
print('R$', sum(meu_total))

print('------------------------------------------------')
print('Seu pedido ficou R$', sum(meu_total))
print(carrinho)
print('------------------------------------------------')

forma_pag  =  [' ','1 - PIX','2 - CC', '3 - CD']
pag =  int(input('ESCOLHA A FORMA DE PAGAMENTO A PARTIR DO ID '))
print('Sua forma de pagamento é', forma_pag[pag], 'Obrigada volte sempre!')



#Split:

M = 'Hello World!'
M = M.split()
print(M)

Separar e tornar um indice de uma lista




#Join:

M = 'Hello World kdflsçkçsld'
delimiter = '-'
N = delimiter.join(M)
print(N)


lista =  list(range(1,31))
print(lista)

minha_tupla = (1, 2, 3, 4, 5)


minha_tupla = (1, 2, 3)

def obter_coordenadas():
    x = 10
    y = 20
    return x, y

coordenadas = obter_coordenadas()
x, y = coordenadas  # Desempacotando os valores da tupla



count(valor): Retorna o número de vezes que um determinado valor aparece na tupla.


tupla = (1, 2, 2, 3, 4, 2)
print(tupla.count(2))  # Saída: 3


index(valor): Retorna o índice da primeira ocorrência de um valor na tupla.


tupla = (1, 2, 3, 4, 5)
print(tupla.index(3))  # Saída: 2


len(tupla): Retorna o número de elementos na tupla.


tupla = (1, 2, 3, 4, 5)
print(len(tupla))  # Saída: 5



sorted(tupla): Retorna uma nova lista ordenada a partir dos elementos da tupla.


tupla = (5, 3, 1, 4, 2)
lista_ordenada = sorted(tupla)
print(lista_ordenada)  # Saída: [1, 2, 3, 4, 5]



max(tupla) e min(tupla): Retorna o maior e o menor valor na tupla, respectivamente.


tupla = (5, 3, 1, 4, 2)
print(max(tupla))  # Saída: 5
print(min(tupla))  # Saída: 1



tuple(iterável): Converte um iterável em uma tupla.


lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla)  # Saída: (1, 2, 3)



unpacking: Permite atribuir os elementos de uma tupla a variáveis individuais.


tupla = (1, 2, 3)
a, b, c = tupla
print(a, b, c)  # Saída: 1 2 3





conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

# União
uniao = conjunto1 | conjunto2  # ou conjunto1.union(conjunto2)
print(uniao)  # Saída: {1, 2, 3, 4, 5, 6}

# Interseção
intersecao = conjunto1 & conjunto2  # ou conjunto1.intersection(conjunto2)
print(intersecao)  # Saída: {3, 4}

# Diferença
diferenca = conjunto1 - conjunto2  # ou conjunto1.difference(conjunto2)
print(diferenca)  # Saída: {1, 2}

# Diferença simétrica
dif_simetrica = conjunto1 ^ conjunto2  # ou conjunto1.symmetric_difference(conjunto2)
print(dif_simetrica)  # Saída: {1, 2, 5, 6}

# Verificar subconjunto
print({1, 2}.issubset(conjunto1))  # Saída: True
print(conjunto1.issuperset({1, 2}))  # Saída: True



# Criando um conjunto com chaves {}
conjunto1 = {1, 2, 3, 4, 5}
print(conjunto1)  # Saída: {1, 2, 3, 4, 5}

# Criando um conjunto com a função set()
	conjunto2 = set([1, 2, 3, 4, 5])
print(conjunto2)  # Saída: {1, 2, 3, 4, 5}

Adicionando Elementos
Para adicionar elementos a um conjunto, utilize o método add().


conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto)  # Saída: {1, 2, 3, 4}

Removendo Elementos
Para remover um elemento de um conjunto, utilize os métodos remove() ou discard(). A diferença entre eles é que remove() gera um erro se o elemento não estiver presente no conjunto, enquanto discard() não gera erro.


conjunto = {1, 2, 3, 4}
conjunto.remove(3)
print(conjunto)  # Saída: {1, 2, 4}

conjunto.discard(2)
print(conjunto)  # Saída: {1, 4}

conjunto.discard(5)  # Não gera erro se o elemento não existir
print(conjunto)  # Saída: {1, 4}

Exemplos Básicos:

#Criando um dicionário vazio:

meu_dicionario = {}
dic = dict{}


#Criando um dicionário com alguns valores:

meu_dicionario = {'a': 1, 'b': 2, 'c': 3}


#Acessando valores usando chaves:

print(meu_dicionario['a'])  # Saída: 1


#Adicionando um novo par chave-valor:

meu_dicionario['d'] = 4
print(meu_dicionario)  # Saída: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


#Removendo um par chave-valor:

del meu_dicionario['a']
print(meu_dicionario)  # Saída: {'b': 2, 'c': 3, 'd': 4}


Principais Métodos:

#`keys()`: Retorna uma lista contendo todas as chaves do dicionário.

print(meu_dicionario.keys())  # Saída: dict_keys(['b', 'c', 'd'])


#`values()`: Retorna uma lista contendo todos os valores do dicionário.

print(meu_dicionario.values())  # Saída: dict_values([2, 3, 4])


#`items()`: Retorna uma lista contendo tuplas de chave-valor.

print(meu_dicionario.items())  
# Saída: dict_items([('b', 2), ('c', 3), ('d', 4)])


#`get()`: Retorna o valor associado à 
chave especificada.

print(meu_dicionario.get('b'))  # Saída: 2


#`pop()`: Remove e retorna o valor 
associado à chave especificada.

valor = meu_dicionario.pop('c')
print(valor)  # Saída: 3
print(meu_dicionario)  # Saída: {'b': 2, 'd': 4}


#`clear()`: Remove todos os itens do dicionário.

meu_dicionario.clear()
print(meu_dicionario)  # Saída: {}




testando dicionarios
alunos = {
    
'nomes':['Ana','Pedro','Julia','Maria'],
'notas':[float(input('nota >')), float(input('nota >')), float(input('nota >')), float(input('nota >'))]

}

media_turma = (alunos['notas'][0] +  alunos['notas'][1] + alunos['notas'][2]+ alunos['notas'][3])/ len(alunos['notas'])

print('média', media_turma)


ecommerce = {
    
    'livros' : {
        
        'A':50.0,
        'B':70.0,
        'C':100.0
     
        },
    'eletronicos':{
        
        'Tablets':3000.0,
        'Fone':150.0,
             
        }
   
    
}

secao1 = input('Digite o seção 1')
secao2 = input('Digite o seção 2')

produto1 = input('Digite o produto 1')
produto2 = input('Digite o produto 2')

carrinho = [produto1, produto2]
valores =  [ecommerce[secao1][produto1],ecommerce[secao2][produto2]]
soma =  sum(valores)

print(carrinho)
print('R$', soma)








