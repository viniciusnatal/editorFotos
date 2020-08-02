#AULA PyQt5 - Criando Interfaces Graficas no Python
import cv2
import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget, QMessageBox
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_main_window()
        self.initUI()

    def setup_main_window(self):
        self.x = 640
        self.y = 480
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Processamento de Imagem")
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.layout = QGridLayout()
        self.wid.setLayout(self.layout)

    def initUI(self):
        #Criando a barr de menu
        self.barrademenu = self.menuBar()

        #Criar os menus
        self.menuarquivo = self.barrademenu.addMenu("&Arquivo")
        self.menutranformacao = self.barrademenu.addMenu("&Transformações")
        self.menuSobre = self.barrademenu.addMenu("&Sobre")


        #Criar as actions

        #Menu Arquivo
        self.opcaoabrir = self.menuarquivo.addAction("&Abrir")
        self.opcaoabrir.triggered.connect(self.open_file)
        #Quando voce usa o open file no action n o lugar de clicked voce coloca triggered
        self.opcaoabrir.setShortcut("Ctrl+A")

        self.menuarquivo.addSeparator()

        self.opcaofechar = self.menuarquivo.addAction("&Fechar Aplicativo")
        self.opcaofechar.setShortcut("Ctrl+X")
        self.opcaofechar.triggered.connect(self.close)

        #Menu Transformaçao
        self.opcaoSharpen = self.menutranformacao.addAction("Transformaçao &Mediana")
        self.opcaoSharpen.setShortcut("Ctrl+S")
        self.opcaoSharpen.triggered.connect(self.transform_me1)
        
        self.menuarquivo.addSeparator()

        self.opcaoEdge = self.menutranformacao.addAction("Filtro &Gaussiano")
        self.opcaoEdge.setShortcut("Ctrl+F")
        self.opcaoEdge.triggered.connect(self.transform_me2)

        self.menuarquivo.addSeparator()

        self.opcaoEdge = self.menutranformacao.addAction("Detecção de &Bordas")
        self.opcaoEdge.setShortcut("Ctrl+D")
        self.opcaoEdge.triggered.connect(self.transform_me3)

        #Menu Sobre
        self.opcaosobre = self.menuSobre.addAction("Desenvolvedor")
        self.opcaosobre.triggered.connect(self.exibe_mensagem)

        self.opcaoInformacao = self.menuSobre.addAction("Informações da Imagem")
        self.opcaoInformacao.triggered.connect(self.exibe_mensagem2)



        #Criar barra de status
        self.barradestatus = self.statusBar()
        self.barradestatus.showMessage("Oi, bem vindo ao meu software", 3000)

        #Criando Label
        self.texto = QLabel("Filtro Negativo from PyQt5 - IFTM", self)
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        
   
        #Criando as imagens
        self.imagem1 = QLabel(self)
        self.endereco1 = 'images/yoda.pgm'
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

        
        self.imagem2 = QLabel(self)
        self.endereco2 = 'images/yoda.pgm'
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

        #organizando os widgets dentro do grid layout
        self.layout.addWidget(self.texto, 0, 0, 1, 2)#layout, linha, coluna/ n° de linhas, n° de colunas
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        self.layout.setRowStretch(0, 0)#posiçao(linha), tamanho do espaço(0-minimo/1-um pouco maior)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 0)

    #metodo para a ações dos botões
    def exibe_mensagem(self):
        #self.barradestatus.showMessage("Voce clicou no sobre...", 5000)
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Desenvolvido por André Nicácio")
        self.msg.setWindowTitle("Sobre")
        self.msg.setInformativeText("Vitória, Instituto Federal do Triangulo Mineiro\n23/06/2020")
        self.msg.setDetailedText("Neste aplicativo foi usado o Filtro Edge, a Transformação Gaussiana e a Transformação Mediana")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec_()# exibir a caixa de mensagens, ou caixa de diálogo
        self.reply = self.msg.clickedButton()
        self.barradestatus.showMessage("Foi clicado o botao: " + self.reply.text())

    def exibe_mensagem2(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Desenvolvido por André Nicácio")
        self.msg.setWindowTitle("Informações da Imagem")
     

        self.entrada = open(self.endereco1, "r+")
        self.linha = self.entrada.readline() #P2
        self.linha2 = self.entrada.readline() #Comentário
        self.linha1 = self.entrada.readline() #Dimensões
        self.dimensoes = self.linha1.split()
        self.largura = self.dimensoes[0]
        self.altura = self.dimensoes[1]


        self.string = self.endereco1
        self.parts = self.string.rpartition('/')
        self.parts2 = self.string.rpartition('.')
        print(self.string)
        print(self.parts)

        self.msg.setDetailedText("Nome: " + self.parts[2] + "\n" + "Extensão do Arquivo: " + self.parts2[2] + "\n" + "Comentario : " + self.linha2 + "\n" + "Largura : " +  self.largura + "\n" + "Altura: " +  self.altura)
        

        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec_()# exibir a caixa de mensagens, ou caixa de diálogo
        self.reply = self.msg.clickedButton()
        self.barradestatus.showMessage("Foi clicado o botao: " + self.reply.text())



    def transform_me1(self):
        self.entrada = self.endereco1
        self.saida = './images/arquivo_novo.pgm'
        self.script = 'transformacao_mediana.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        
    def transform_me2(self):
        self.entrada = self.endereco1
        self.saida = 'images/arquivo_novo.pgm'
        self.script = 'transformacao_gaussiana.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def transform_me3(self):
        self.entrada = self.endereco1
        self.saida = 'images/arquivo_novo.pgm'
        self.script = 'filtro_edge.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)              

    def open_file(self): 
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption = 'Open Image', directory=QtCore.QDir.currentPath(), filter='All files (*.*);;Images (*.ppm;*.pgm;*.pbm)', initialFilter='Images (*.ppm;*.pgm;*.pbm;)')
        if fileName != '':
            self.endereco1 = fileName
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
            self.imagem1.setPixmap(self.pixmap1)        
        
        print(fileName)
    

    def button_clicked(self):
        self.texto.setText("Voce clicou no Botao!!")
        self.texto.adjustSize()
        self.novoEndereco = QtGui.QPixmap("balao.pgm")
        self.imagem1.setPixmap(self.novoEndereco)
        self.imagem2.setPixmap(self.novoEndereco)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

    print(sys.argv)

window()

