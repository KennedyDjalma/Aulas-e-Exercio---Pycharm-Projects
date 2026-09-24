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


#   DEFINIÇÃO DE FUNÇÃO

def mensagem(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


mensagem('Olá, Mundo!')
mensagem('Kennedy Djalma')