# https://www.youtube.com/watch?v=ezfr9d7wd_k&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=117

'''
#1 EXEMPLOS DE FUNÇÃO
def mostraLinha():
    print('-' * 30)

mostraLinha()
print('Sistema de aula 20')
mostraLinha()
'''

'''
#2 EXEMPLOS DE FUNÇÃO
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

mensagem('SISTEMA DE AULA 20')
# pode-se colocar mais mensagens no print. EX:
mensagem('2 EXEMPLOS DE FUNÇÃO')
'''

'''
def soma(a,b):
    s = a + b
    print(s)

#PROGRAMA PRINCIPAL
soma(4,5)
soma(8,9)
soma(2,1)
'''

'''
def contador(*num):
    print(num)

contador(5,7,3,1,4)
contador(8,0,6)
'''

'''
def contador(*num):
    for valor in num:
        print(valor, end=' ')
    print()

contador(5,7,3,1,4)
contador(8,0,6)
'''

'''
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(5,7,3,1,4)
contador(8,0,6)
'''

'''
def dobra(lst):
    pos = 0
    while pos < len(lst): #enquanto posição for menor que alista
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''

'''
def soma(*valores):
    s = 0
    for numero in valores:
        s += numero
    print(f'Somando os valores {valores}, temos {s}')


soma(5, 2)
soma(2, 9, 4)
'''

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
EXERCICIO 96
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA AREA(), QUE
RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR(LARGURA E
COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO.
'''

'''
EXERCICIO 97
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO ESCREVA(), QUE RECEBA
UM TEXTO QUALQUER COMO PARÂMETRO E MOSTRE UMA MENSAGEM COM
TAMANHO ADAPTAVEL.
EX: ESCREVA('Olá, mundo!')
SAIDA:
-----------------
Olá, mundo!
-----------------
'''

'''
EXERCICIO 98
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR()
QUE RECEBA TRES PARAMETROS: INICIO, FIM E PASSO, E REALIZE
A CONTAGEM.
- SEU PROGRAMA TEM QUE REALIZAR TRES CONTAGENS ATRAVES
DA FUNÇÃO CRIADA:
A - DE 1 ATÉ 10, DE 1 EM 1.
B - DE 10 ATÉ 0, DE 2 EM 2.
C - UMA CONTAGEM PERSONALIZADA.
'''

'''
EXERCICIO 99
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(),
QUE RECEBA VÁRIOS PARAMETROS COM VALORES INTEIROS.
SEU PROGRAMA TEM QUE ANALIZAR TODOS OS VALORES E DIZER 
QUAL DELES É O MAIOR.
'''

'''
EXERCICIO 100
FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS
E DUAS FUNÇÕES CHAMADAS SORTEIA() E SOMAPAR().
A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NUMEROS E VAI COLOCALOS
DENTRO DA LISTA E A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA
ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO
ANTERIOR.
'''