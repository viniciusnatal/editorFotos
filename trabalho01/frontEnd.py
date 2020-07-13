import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget, QMessageBox
from PyQt5.QtCore import QSize


class MyWindow(QMainWindow):
    def __init__(self):
        super( MyWindow, self ).__init__()
        self.setup_main_window()
        self.initUI()

    def setup_main_window(self):
        self.setFixedSize(640, 480)
        self.x = 640
        self.y = 480
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Choque e Natal Photos")
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.layout = QGridLayout()
        self.wid.setLayout(self.layout)

    def initUI(self):
        # Criando a barr de menu
        self.barrademenu = self.menuBar()

        # Criar os menus
        self.menuarquivo = self.barrademenu.addMenu("&Arquivo")
        self.menutranformacao = self.barrademenu.addMenu("&Filtros")
        self.menuSobre = self.barrademenu.addMenu("&Sobre")

        # Criar as actions >> Menu Arquivo
        self.opcaoabrir = self.menuarquivo.addAction("&Abrir Imagem")
        self.opcaoabrir.triggered.connect(self.open_file)
        self.opcaoabrir.setShortcut("Ctrl+O")

        self.menuarquivo.addSeparator()

        self.opcaofechar = self.menuarquivo.addAction( "&Salvar como..." )
        self.opcaofechar.setShortcut( "Ctrl+S" )

        self.menuarquivo.addSeparator()

        self.opcaofechar = self.menuarquivo.addAction("&Fechar Aplicação")
        self.opcaofechar.setShortcut("Ctrl+X")
        self.opcaofechar.triggered.connect(self.close)


        # Menu Transformaçao
        self.opcaoSharpen = self.menutranformacao.addAction("&Negativo")
        self.opcaoSharpen.setShortcut("Ctrl+1")
        #self.opcaoSharpen.triggered.connect( self.transform_me1 )

        self.menutranformacao.addSeparator()

        self.opcaoSharpen = self.menutranformacao.addAction( "&Transformação Logarítmica" )
        self.opcaoSharpen.setShortcut( "Ctrl+2" )
        # self.opcaoSharpen.triggered.connect( self.transform_me1 )

        self.menutranformacao.addSeparator()

        self.opcaoSharpen = self.menutranformacao.addAction( "&Correção Gamma" )
        self.opcaoSharpen.setShortcut( "Ctrl+3" )
        # self.opcaoSharpen.triggered.connect( self.transform_me1 )

        self.menutranformacao.addSeparator()

        self.opcaoSharpen = self.menutranformacao.addAction( "&Filtro Sharpen" )
        self.opcaoSharpen.setShortcut( "Ctrl+4" )
        # self.opcaoSharpen.triggered.connect( self.transform_me1 )

        self.menutranformacao.addSeparator()

        self.opcaoSharpen = self.menutranformacao.addAction( "&Filtro Mediano" )
        self.opcaoSharpen.setShortcut( "Ctrl+5" )
        # self.opcaoSharpen.triggered.connect( self.transform_me1 )

        self.menutranformacao.addSeparator()

        self.opcaoSharpen = self.menutranformacao.addAction( "&Filtro Gaussiano" )
        self.opcaoSharpen.setShortcut( "Ctrl+6" )
        # self.opcaoSharpen.triggered.connect( self.transform_me1 )

        # Menu Sobre
        self.opcaosobre = self.menuSobre.addAction("Info Alunos")
        self.opcaosobre.triggered.connect(self.exibe_mensagem)

        self.menuSobre.addSeparator()

        self.opcaosobre2 = self.menuSobre.addAction("Infos Imagem")
        self.opcaosobre2.triggered.connect(self.exibe_mensagem2)

        # Criar barra de status
        self.barradestatus = self.statusBar()
        self.barradestatus.showMessage("Seja bem vindo ao NatalPhoto's ", 2000)

        # Criando Label
        self.texto = QLabel("PDI: Lista 13 - Vinícius Natal Gonçalves", self)
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment( QtCore.Qt.AlignCenter )

        # Criando as imagens
        self.imagem1 = QLabel(self)
        self.endereco1 = 'images/narutin.jpg'
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

        self.imagem2 = QLabel(self)
        self.endereco2 = 'images/narutin.jpg'
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled( 300, 300, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap(self.pixmap2)
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

        # Organizar Widgets
        self.layout.addWidget(self.texto, 0, 0, 1, 2)
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        self.layout.setRowStretch(0, 0)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 0)

        # Açao dos botoes
    def exibe_mensagem(self):
        self.msg = QMessageBox()
        self.msg.setIcon( QMessageBox.Information )
        self.msg.setText( "Desenvolvido por: \nAndré Nicácio e Vinícius Natal" )
        self.msg.setWindowTitle( "Sobre os alunos " )
        self.msg.setDetailedText(
            "Data de término do projeto:  \n "
            "Link do vídeo: \n"
            "IItuiutaba, Instituto Federal do Triangulo Mineiro")
        self.msg.setStandardButtons( QMessageBox.Ok | QMessageBox.Cancel )
        self.msg.exec_()  # exibir a caixa de mensagens, ou caixa de diálogo
        self.reply = self.msg.clickedButton()

    def exibe_mensagem2(self):
        self.msg = QMessageBox()
        self.msg.setIcon( QMessageBox.Information )
        self.msg.setText( "Informações do Arquivo " )
        self.msg.setWindowTitle( "Sobre a Imagem" )
        self.msg.setDetailedText(
            "Nome do Arquivo:  \n"
            "Tipo do Arquivo: \n"
            "Comentário: \n"
            "Largura:  " 
            "Altura:  ")
        self.msg.setStandardButtons( QMessageBox.Ok | QMessageBox.Cancel )
        self.msg.exec_()  # exibir a caixa de mensagens, ou caixa de diálogo
        self.reply = self.msg.clickedButton()


    def transform_me1(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfAbertura.pgm'
        self.script = 'abertura.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled( 300, 300, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap(self.pixmap2)

    def transform_me2(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfGaussiano.pgm'
        self.script = 'gaussiano.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def transform_me3(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfFechamento.pgm'
        self.script = 'fechamento.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def open_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName( self, caption='Abrir Imagem',
                                                             directory=QtCore.QDir.currentPath(),
                                                             filter='Todos os Tipos (*);;Images (*.ppm;*.pgm;*.pbm; *.jpg; *.png)',
                                                             initialFilter='Images (*.ppm;*.pgm;*.pbm;*.jpg;*.png;)' )
        if fileName != '':
            self.endereco1 = fileName
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
            self.imagem1.setPixmap(self.pixmap1)

        print(fileName)

    def button_clicked(self):
        self.texto.setText("Voce clicou no Botao!")
        self.texto.adjustSize()
        self.novoEndereco = QtGui.QPixmap("narutin.pgm")
        self.imagem1.setPixmap(self.novoEndereco)
        self.imagem2.setPixmap(self.novoEndereco)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

    print(sys.argv)


window()

