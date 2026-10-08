# -----------------------------------------------------
''' EXERCÍCIO 103
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA()
QUE RECEBA DOIS PARAMETROS OPCIONAIS: O NOME DE UM
JOGADOR E QUANTOS GOLS ELE MARCOU.
O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO
JOGADOR, MESMO QUE ALGUM DADO NÃO TENHA SIDO INDORMADO
CORRETAMENTE.
'''
# -----------------------------------------------------



def ficha(jogador='<Desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gol} gols.')



    # PROGRAMA PRINCIPAL
n = str(input("NOME DO JOGADOR: "))
g = str(input("Número de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
