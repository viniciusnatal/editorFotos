# -*- coding: utf-8 -*-
import numpy as np
import math
import sys

entrada = open(sys.argv[1], "rb+")
saida = open(sys.argv[2], "wb+")

linha = entrada.readline() # P1
linha = entrada.readline() # Comentário
linha = entrada.readline() # Dimensões da imagem
dimensoes = linha.split() # Lista com as dimensões
largura = int(dimensoes[0])
altura = int(dimensoes[1])
dimensoes = np.asarray(dimensoes, dtype=int) # Converte a lista para um array

linhas = entrada.readlines() # lê todo o restante do arquivo
linhas = [x.strip() for x in linhas] # remove o \n do final de todas as linhas


def concatenate_list_data(list):
    result = ''
    for element in list:
        result += str(element)
    return result


#concatena todos os elementos em uma única string
longstring = concatenate_list_data(linhas)
#converte a string longa para um array de uma dimensão
image = np.array(list(longstring))
#muda a forma do array de [altura*largura, 1] para [altura, largura]
image = np.reshape(image, [dimensoes[1], dimensoes[0]])
#converte a matriz para inteiro
image = image.astype(int)

#Elemento Estruturante 3x3
estruturante = [[0, 0, 0], [0, 1, 1], [0, 0, 0]]



#Array numpy do elemento estruturante
estruturante = np.asarray(estruturante)


#Pegar pixel posição pixel central
pixel = int((len(estruturante) - 1) / 2)

#escrevendo a imagem cópia
saida.write("P1\n")
saida.write("#Criado por \n")
saida.write(str(largura))
saida.write(" ")
saida.write(str(altura))
saida.write("\n")


image2 = image.copy()

for i in range(pixel, len(image) - pixel):
    for j in range(pixel, len(image[1]) - pixel):
        for x in range(len(estruturante)):
            for y in range(len(estruturante[1])):
                if image[i][j] == 0 and estruturante[x][y] == 1:
                    image2[i - pixel + x][j - pixel + y] = 0

for i in range(len(image)):
    image2[i] = image[i] - image2[i]

print(image2)

for l in range(len(image2)):
    for c in range(len(image2[1])):
        saida.write(str(image2[l][c]))
    saida.write("\n")


# fechar os dois arquivos.
entrada.close()
saida.close()
