# -----------------------------------------------------
''' EXERCÍCIO 102
CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL() QUE
RECEBA DOIS PARAMETROS: O PRIMEIRO QUE INDIQUE O NUMERO
A CALCULAR E O OUTRO CHAMADO SHOW,QUE SERA UM VALOR
LOGICO (OPCIONAL) INDICANDO SE SERA MOSTRADO OU NAO
NA TELA O PROCESSO DE CALCULO FATORIAL.
'''


# -----------------------------------------------------
def fatorial(numero, show=False):
    """
    -> CALCULANDO FATORIAL DE UM NÚMERO.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número.
    """
    f = 1
    for c in range(numero, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
    f *= c
    return f


print(fatorial(5, show=True))
# help(fatorial)
