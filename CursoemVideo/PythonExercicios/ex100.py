'''
EXERCICIO 100
FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS
E DUAS FUNÇÕES CHAMADAS SORTEIA() E SOMAPAR().
A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NUMEROS E VAI COLOCALOS
DENTRO DA LISTA E A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA
ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO
ANTERIOR.
'''

from random import randint

def sorteia(lista):
    print('Sorteando os valores...', end=' ')

    for contador in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end=' ')
    print('FIM')


def somaPar(lista):
    soma = 0

    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma} ')

numeros = list()
sorteia(numeros)
somaPar(numeros)
