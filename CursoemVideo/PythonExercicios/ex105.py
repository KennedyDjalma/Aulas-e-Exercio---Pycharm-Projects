# -----------------------------------------------------
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
# -----------------------------------------------------

def notas(*n, sit=False):
    """
    -> FUNÇÃO PARA ANALIZAR NOTAS E SITUAÇÃO DE VARIOS ALUNOS.
    :param n:       UMA OU MAIS NOTAS DOS ALUNOS (ACEITA VARIÁVEIS).
    :param sit:     VALOR OPCIONAL, INNDICANDO SE DEVE OU NÃO ADICIONAR A SITUAÇÃO.
    :return:        DICIONÁRIO COM VÁRIAS INFORMAÇÕES DA TURMA.
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


        # PROGRAMA PRINCIPAL
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
#help(notas)
