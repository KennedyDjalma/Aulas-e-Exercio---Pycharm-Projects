# https://www.youtube.com/watch?v=vp9UX7wr92o&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=121
'''
EXERCICIO 99
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(),
QUE RECEBA VÁRIOS PARAMETROS COM VALORES INTEIROS.
SEU PROGRAMA TEM QUE ANALIZAR TODOS OS VALORES E DIZER
QUAL DELES É O MAIOR.
'''

from time import sleep


def maior(* numeros):
    contador = maior = 0

    print('-=' * 20)
    print('\nAnalisando os valores passados...')
    for valor in numeros:
        print(f'{valor} ', end='')
        sleep(0.4)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'\nForam informados {contador} valores.')
    print(f'\nO maior valor informado foi {maior}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
