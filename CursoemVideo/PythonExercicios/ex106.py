# -----------------------------------------------------
''' EXERCÍCIO 106
FAÇA UM MINI-SISTEMA QUE UTILIZE O INTERACTIVE HELP
DO PYTHON. O USUARIO VAI DIGITAR O COMANDO E O MANUAL
VAI APARECER. QUANDO O USUARIO DIGITAR 'FIM', O PROGRAMA
SE ENCERRARÁ.
OBS: USE CORES.
'''
# -----------------------------------------------------
    #   LISTA GLOBAL, PODE UTILIZAR NO PROGRAMA INTEIRO
c = ('\033[0m',        # 0 = sem cor
     '\033[0;30;41m',  # 1 = vermelho
     '\033[0;30;42m',  # 2 = verde
     '\033[0;30;43m',  # 3 = amarelo
     '\033[0;30;44m',  # 4 = azul
     '\033[0;30;45m',  # 5 = roxo
     '\033[0;47m'      # 6 = branco
     '\033[0;37m'      # 7 = TEXTO branco
     );

    #   COMANDO AJUDA
def ajuda(Comando):
    titulo(f'Acessando o manual do comando \'{Comando}\'', 4)
    print(c[3], end='')
    help(Comando)
    print(c[0], end='')

    #    FUNÇÃO TÍTULO PERSONALIZADO AO TAMANHO DA MSG
def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(msg.center(tamanho))  # .center(tamanho) =>  CENTRALIZA A MSG ENTRE OS ~
    print('~' * tamanho)
    print(c[0], end='')


#       programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO ...', 1)
