#Transformações espaciais
# Máscaras (Kernel) - Gaussiana, Mediana(BoxBlur), Sharpen, Edge Detection
import numpy as np
import math
import sys

entrada = open(sys.argv[1], "r+")
saida = open(sys.argv[2], "w+")

linha = entrada.readline() #P2
linha = entrada.readline() #Comentário
linha = entrada.readline() #Dimensões
dimensoes = linha.split()
largura = int(dimensoes[0])
altura = int(dimensoes[1])
linha = entrada.readline() #Valar fixo
linha = entrada.readlines() #Ler o restante do arquivo e gravar como lista

#converter de lista para array
imagem = np.asarray(linha, dtype=int)
#reshape
imagem = np.reshape(imagem, (altura, largura))

#Gaussiana 3x3
#kernel = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
#kernel = np.asarray(kernel)/16

#Gaussiana 5x5
#kernel = [[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4], [1, 4, 7, 4, 1]]
#kernel = np.asarray(kernel)/273

#Gaussiana 7x7
#kernel = [[0, 0, 1, 2, 1, 0, 0], [0, 3, 13, 22, 13, 3, 0], [1, 13, 59, 97, 59, 13, 1], [2, 22, 97, 159, 97, 22, 2],
#          [1, 13, 59, 97, 59, 13, 1], [0, 3, 13, 22, 13, 3, 0], [0, 0, 1, 2, 1, 0, 0]]
#kernel = np.asarray(kernel)/1003

#Mediana(BoxBlur)
#kernel = np.ones((3,3))
#kernel = np.asarray(kernel)/9

#Edge Detection
#kernel = [[1, 0, -1], [0, 0, 0], [-1, 0, 1]]
#kernel = np.asarray(kernel)

#kernel = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
#kernel = np.asarray(kernel)

#kernel = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
#kernel = np.asarray(kernel)

#Sharpen
kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
kernel = np.asarray(kernel)

print(kernel)

ks = int((len(kernel) - 1) / 2)
print(ks)

#escrevendo a imagem cópia
saida.write("P2\n")
saida.write("#Criado por André\n")
#saida.write(str(largura-2))
saida.write(str(largura-(ks*2)))
saida.write(" ")
saida.write(str(altura-(ks*2)))
#saida.write(str(altura-2))
saida.write("\n")
saida.write("255\n")

#fazer a transformação
for i in range(ks, len(imagem)-ks):
    for j in range(ks, len(imagem[1])-ks):
        sum = 0
        for ki in range(len(kernel)):
            for kj in range(len(kernel[1])):
                sum = sum + (imagem[i-1+ki][j-1+kj]*kernel[ki][kj])
                #sum = sum + (imagem[i - ks + ki][j - ks + kj] * kernel[ki][kj])
        sum = int(sum)
        sum = str(sum)
        saida.write(sum)
        saida.write("\n")

#fechar os dois arquivos
entrada.close()
saida.close()