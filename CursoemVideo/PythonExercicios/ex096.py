'''
EXERCICIO 96
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA AREA(), QUE
RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR(LARGURA E
COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO.
'''


def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg} x {comp} é de {a}m². ')


print('CONTROLE DE TERRENOS')
print('~~' * 20)
l = float(input('LARGURA: '))
c = float(input('COMPRIMENTO: '))
area(l, c)