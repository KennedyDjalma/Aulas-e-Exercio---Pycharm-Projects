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
from time import sleep

def contador(i, f, p):
    print('-~' * 20)
    print(f'Contagem de {i} ate {f} de {p} em {p}.')
    sleep(1)

    if p < 0: # se passo for menor que zero
        p *= -1 # passo x passo -1 (numero fica positivo).
    if p == 0: # se passo for zero
        p = 1   # o passo começa com 1

    if i < f: # A - DE 1 ATÉ 10, DE 1 EM 1.
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('fim')

    else: # B - DE 10 ATÉ 0, DE 2 EM 2.
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('fim')
    print('-~' * 20)

contador(1, 10, 1)
contador(10, 0, 2)
print('-~' * 20)

# C - UMA CONTAGEM PERSONALIZADA.
print('AGORA É SUA VEZ DE PERSONALIZAR A  CONTAGEM!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)

