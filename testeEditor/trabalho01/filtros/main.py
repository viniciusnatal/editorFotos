
import numpy as np
import math

#abrir o arquivo original e a cópia
entrada = open("images/yoda.pgm", "r+")
saida = open("images/yoda_pbm.pbm", "w+")

linha = entrada.readline() #P3
linha = entrada.readline() #Comentário
linha = entrada.readline() #Dimensões
dimensoes = linha.split()
largura = int(dimensoes[0])
altura = int(dimensoes[1])
linha = entrada.readline() #Valor fixo
linha = entrada.readlines() #Ler o restante do arquivo e grava como lista

#converter de lista para array
imagem = np.asarray(linha, dtype=float)
#reshape
imagem = np.reshape(imagem, (altura, largura))
#print(imagem)
#print(imagem.shape)
#print(len(imagem))
#print(len(imagem[1]))

#escrevendo a imagem cópia
saida.write("P1\n")
saida.write("#Criado por Andre\n")
saida.write(str(largura))
saida.write("\n")
saida.write(str(altura))
saida.write("\n")
#saida.write("255\n")


limite = 128
#fazer a cópia
for i in range(len(imagem)):
    for j in range(len(imagem[1])):
        if imagem[i][j] > limite:
            saida.write("1")
        else:
            saida.write("0")
        saida.write("\n")

#fechar os dois arquivos.
entrada.close()
saida.close()
