# -----------------------------------------------------
''' EXERCÍCIO 101
CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO()
QUE VAI RECEBER COMO PARAMETRO O ANO DE NASCIMENTO
DE UMA PESSOA, RETORNANDO UM VALOR LITERAL INDICANDO
SE UMA PESSOA TEM VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO
NAS ELEIÇÕES.
'''


# -----------------------------------------------------


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# programa principal
nas = int(input('Em que ano você nasceu??'))
print(voto(nas))
