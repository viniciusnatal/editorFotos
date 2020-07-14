# colorido: PPM
# escala de cinza : PGM
# preto e branco: PBM
#
#
# sintaxe desses arquivos
# primeira linha: código que representa a cor
# P1 - imagens em preto e branco
# P2 - imagens em escla de cinza
# P3 - imagens coloridas
#
# segunda linha: #comentário
#
# terceira linha: dimensões da imagem (largura x altura - em pixel)
#
# quarta linha: valor fixo (255) - valor máximo do pixel
#
# quinta linha (pixels da imagem):
# PBM: 0 para branco e 1 para preto, um valor para cada pixel
# PGM: 0 para preto. 255 para branco, um valor para cada pixel
# PPM: a cada três valores, forma um pixel

#Transformações de intensidade
#Negativo

#abrir o arquivo original e a cópia

import numpy as np
import math
import sys

entrada = open(sys.argv[1], "r+")
saida = open(sys.argv[2], "w+")

linha = entrada.readline() #P2
linha = entrada.readline() #comentário
linha = entrada.readline() #Dimensões
dimensoes = linha.split()
largura = dimensoes[0]
altura = dimensoes[1]
print(largura, altura)
linha = entrada.readline() #Valor fixo

linha = entrada.readlines() # ler o restante do arquivo e grava como lista

#converter de lista para array
imagem = np.asarray(linha, dtype=int)
print(imagem)

#escrevendo a imagem cópia
saida.write("P2\n")
saida.write("#Criado por Thais\n")
saida.write(largura)
saida.write(" ")
saida.write(altura)
saida.write("\n")
saida.write("255\n")

#fazer a transformação de intesidade (negativo)
for i in range((len(imagem))):
    n = 255 - imagem[i]
    n = str(n)
    saida.write(n) #este comando write só aceita string, por isso foi preciso converter
    saida.write("\n")
    # estamos jogando em uma array, se fosse utilizarmos a distância euclidiana precisamos de matriz


print(type(linha)) # do tipo lista <class 'list'>
print(len(linha)) # tamanho 373700


#fechar os dois arquivos
entrada.close()
saida.close()