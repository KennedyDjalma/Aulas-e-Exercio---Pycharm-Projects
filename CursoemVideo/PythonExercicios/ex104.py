# -----------------------------------------------------
''' EXERCÍCIO 104
CRIE UM PROGRAMA QUE TENHA A FUNÇÃO LEIAINT(), QUE VAI
FUNCIONAR DE FORMA SEMELHANTE A FUNCAO INPUT() DO PY,
SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS UM VALOR
NUMERICO.
EX:
n = leiaint('Digite um numero: ')
'''


# -----------------------------------------------------

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO!, digite um numero inteiro válido\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o número {n}')
