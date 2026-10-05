# https://www.youtube.com/watch?v=etjJ_4Eqrk8&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=123

# FUNÇÕES 2
'''
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de 3 valores e mostra o resultado.
    :Parametro a: O primeiro valor
    :Parametro b: O segundo valor
    :Parametro c: O terceiro valor
    Funcao criada por Kennedy.
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 1)
'''

'''
def teste():
    x = 8
    print(f'NA FUNÇÃO TESTE, O N VALE {n}')
    print(f'NA FUNÇÃO TESTE, O X VALE {x}')
    
#programa pricipal
n = 2
print(f'NA FUNÇÃO PRINCIPAL, O N VALE {n}')
teste()
print(f'NA FUNÇÃO PRINCIPAL, O X VALE {x}')
'''

'''
def funcao():
    n1 = 4
    print(f'n1 DENTRO vale {n1}')

n1 = 2
funcao()
print(f'n1 FORA vale {n1}')
'''

'''
def fatorial(numero=1):
    f = 1
    for c in range(numero, 0, - 1):
        f *= c
    return f

n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print('-/' *40)
print(f'OS RESULTADOS {f1} e {f2} e {f3}')
'''

'''
def par(numero=0):
    if numero % 2 == 0:
        return True
    else:
        return False


numero = int(input('Digite um numero: '))
if par(numero):
    print('É PAR')
else:
    print('É IMPAR')
'''

#-----------------------------------------------------
''' EXERCÍCIO 101
CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO()
QUE VAI RECEBER COMO PARAMETRO O ANO DE NASCIMENTO
DE UMA PESSOA, RETORNANDO UM VALOR LITERAL INDICANDO
SE UMA PESSOA TEM VOTO NEGADO, OPCIONAL OU OBRIGATORIO
NAS ELEIÇÕES.
'''
#-----------------------------------------------------
''' EXERCÍCIO 102
CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL() QUE
RECEBA DOIS PARAMETROS: O PRIMEIRO QUE INDIQUE O NUMERO
A CALCULAR E O OUTRO CHAMADO SHOW,QUE SERA UM VALOR
LOGICO (OPCIONAL) INDICANDO SE SERA MOSTRADO OU NAO
NA TELA O PROCESSO DE CALCULO FATORIAL.
'''
#-----------------------------------------------------
''' EXERCÍCIO 103
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA()
QUE RECEBA DOIS PARAMETROS OPCIONAIS: O NOME DE UM
JOGADOR E QUANTOS GOLS ELE MARCOU.
O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO 
JOGADOR, MESMO QUE ALGUM DADO NÃO TENHA SIDO INDORMADO
CORRETAMENTE.
'''
#-----------------------------------------------------
''' EXERCÍCIO 104
CRIE UM PROGRAMA QUE TENHA A FUNÇÃO LEIAINT(), QUE VAI
FUNCIONAR DE FORMA SEMELHANTE A FUNCAO INPUT() DO PY,
SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS UM VALOR
NUMERICO.
EX:
n = leiaint('Digite um numero: ')
'''
#-----------------------------------------------------
''' EXERCÍCIO 105
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS() QUE PODE
RECEBER VARIAS NOTAS DE ALUNOS E VAI RETORNAR UM
DICIONARIO COM AS SEGUINTES INFORMAÇÕES:

-QUANTIDADE DE NOTAS
-A MAIOR NOTA
-A MENOR NOTA
-A MEDIA DA TURMA
-A SITUAÇÃO (OPCIONAL)

ADICIONE TAMBEM AS DOCSTRINGS DA FUNÇÃO.
'''
#-----------------------------------------------------
''' EXERCÍCIO 106
FAÇA UM MINI-SISTEMA QUE UTILIZE O INTERACTIVE HELP
DO PYTHON. O USUARIO VAI DIGITAR O COMANDO E O MANUAL
VAI APARECER. QUANDO O USUARIO DIGITAR 'FIM', O PROGRAMA
SE ENCERRARÁ.
OBS: USE CORES.
'''
#-----------------------------------------------------