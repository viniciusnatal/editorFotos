import numpy as np

#abrir o arquivo original e a cópia
entrada = open("original.ppm", "r+")
saida = open("pb_192.pbm", "w+")

linha = entrada.readline() #P3
linha = entrada.readline() #Comentário
linha = entrada.readline() #Dimensões
dimensoes = linha.split()
largura = int(dimensoes[0])
altura = int(dimensoes[1])
linha = entrada.readline() #Valor fixo
linha = entrada.readlines() #Ler o restante do arquivo e grava como lista

#converter de lista para array
imagem = np.asarray(linha, dtype=int)
#reshape
imagem = np.reshape(imagem, (altura, largura, 3))

linhas = []

#converter pixels coloridos para escala de cinza
for i in range(len(imagem)):
    for j in range(len(imagem[1])):
        sum = 0
        for k in range(3):
            sum = sum + imagem[i][j][k]
        sum = int(sum / 3)
        sum = str(sum)
        linhas.append(sum)

#converter de lista para array
img = np.asarray(linhas, dtype=int)
#reshape
img = np.reshape(img, (altura, largura))

#escrevendo a imagem cópia
saida.write("P1\n")
saida.write("#Criado por Thais\n")
saida.write(str(largura))
saida.write(" ")
saida.write(str(altura))
saida.write("\n")
limite = 192

#fazer a cópia para imagem binária
for i in range(len(img)):
    for j in range(len(img[1])):
        if img[i][j] > limite:
            saida.write("0")
        else:
            saida.write("1")
        saida.write("\n")

#fechar os dois arquivos.
entrada.close()
saida.close()