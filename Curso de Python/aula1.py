'''

Tipo de dados (Data Type):

- texto
string= str ("texto")

- numero
integer (int)= inteiro (1 , 2 , 3, 4)
float = fração (1.3 , 2.30)

Tipo Boolean 

-true
-false

Variaveis (Conteiner para colocar dados)

-If
-elif
-else


Métodos para Strings:

.lower() = tudo em letra minuscula
.upper() = tudo em letra maiuscula
.capitalize() = pega a primeira letra da string e coloca em maiuscula
.find() = 
.replace() = ele troca as letras/palavras da string
exemplo:
mensagem= 'Eu adoro comida caseira'
print(mensagem.replace('a','e'))
saida: Eu edore comide ceseire


.strip() = ele retira os espaços que o usuario coloca antes da string.

'''

# idade= int(input("Digite sua idade\n"))
# resultado= 'Voto permitido' if idade >= 16 else 'Voto não permitido'
# print(resultado)

# idade= int(input("Digite sua idade\n"))

# if idade >=16:
#     print("Voto permitido")
# else:
#     print("Não permitido votar")    


# for loop - para numeros
# for numero in range(1,30,2):
#     print(numero)
# range= quantidade de vezes que o numero vai rodar.
# se colocar (1,6,2 {esse ultimo 2, indica pro codigo pular de 2 em 2})

# for loop - para strings

# for letra in 'Google':
#     print(letra)

# compra_confirmada= True
# dados_compra= "Compra no valor de R$ 12,50 e entrega confirmada"

# for enviar in range(3):
#     if compra_confirmada:
#         print(dados_compra)
#         print('Detalhes enviado para o seu email')
#         break
#     else:
#         print('Falha na compra')

# for loop nested
#   outer loop = loop de fora
#   inner loop = loop de dentro

# for numero1 in range(5):
#     print(f'produto {numero1}')
#     for numero2 in range(5):
#         print(f'{numero2}')

# Modificar a palavra FANTASTICO para F A N T A S T I C O

# palavra= 'Fantastico'
# for spaco in palavra:
#     print(f' {spaco}' , end='')

# Criar um retangulo em código 6x6 usando @
# @@@@@@
# @@@@@@
# @@@@@@
# @@@@@@
# @@@@@@
# @@@@@@

# linhas= 6
# colunas=6
# simbolo='@'

# for l in range(linhas):
#     for c in range(colunas):
#         print(simbolo, end='')
#     print()    


# cidades=['Rio de Janeiro', 'São Paulo', 'Porto Alegre']

# # .append insere um item no final da lista
# # .romeve - remove um item da lista
# # .insert - insere um item na posição correta, exemplo: cidades.insert(1,'Floripa')
# # .sort - organiza em ordem alfabética



# print(cidades)