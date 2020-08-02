import numpy as np
import math

entrada = open("tucano.pgm", "r+")
saida = open("tucanocopialog.pgm", "w+")

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
# fator gama


#fazer a transformação
for i in range((len(imagem))):
    n = int((math.log(1 + (imagem[i]/255)))*255)
    n = str(n)
    saida.write(n)
    saida.write("\n")



print(type(linha))
print(len(linha))


#fechar os dois arquivos
entrada.close()
saida.close()