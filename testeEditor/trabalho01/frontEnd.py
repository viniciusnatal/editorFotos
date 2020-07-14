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
        self.x = 800
        self.y = 600
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
        self.menuFiltros = self.barrademenu.addMenu("&Filtros")
        self.menuTransf = self.barrademenu.addMenu("&Transformações")
        self.menuSobre = self.barrademenu.addMenu("&Sobre")

        # Criar as actions >>
        ##MENU ARQUIVOS COMEÇA AQUI ------------------------------------------------------#
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
        ##MENU ARQUIVOS TERMINA AQUI ------------------------------------------------------#

        ##MENU FILTROS COMEÇA AQUI ------------------------------------------------------#
        self.opcaoNegativo = self.menuFiltros.addAction("&Negativo")
        self.opcaoNegativo.setShortcut("Ctrl+1")
        self.opcaoNegativo.triggered.connect( self.transform_me1 )#====================================================NEGATIVO

        self.opcaoGamma = self.menuFiltros.addAction( "&Correção Gamma" )
        self.opcaoGamma.setShortcut( "Ctrl+2" )
        self.opcaoGamma.triggered.connect( self.transform_me2 )#========================================================GAMA

        self.opcaoSharpen = self.menuFiltros.addAction( "&Sharpen" )
        self.opcaoSharpen.setShortcut( "Ctrl+3" )
        self.opcaoSharpen.triggered.connect( self.transform_me3 )#=========================================================SHARPEN

        self.opcaoMediana = self.menuFiltros.addAction( "&Mediana" )
        self.opcaoMediana.setShortcut( "Ctrl+4" )
        self.opcaoMediana.triggered.connect( self.transform_me4 )#============================================================MEDIANA

        self.opcaoGaussiano = self.menuFiltros.addAction( "&Gaussiano" )
        self.opcaoGaussiano.setShortcut( "Ctrl+5" )
        self.opcaoGaussiano.triggered.connect( self.transform_me5 )#============================================================GAUSSIANO

        self.menuFiltros.addSeparator()

        self.opcaoCinza = self.menuFiltros.addAction( "Escala cinza" )
        self.opcaoCinza.setShortcut( "Ctrl+6" )
        self.opcaoCinza.triggered.connect( self.transform_me6 )#==========================================================================ESCALA DE CINZA

        self.opcaoPeB = self.menuFiltros.addAction( "Preto e branco" )
        self.opcaoPeB.setShortcut( "Ctrl+7" )
        self.opcaoPeB.triggered.connect( self.transform_me7 )

        self.opcaoSepararRed = self.menuFiltros.addAction( "Separar camada: Vermelho" )
        self.opcaoSepararRed.setShortcut( "Ctrl+8" )
        self.opcaoSepararRed.triggered.connect( self.transform_me8 )

        self.opcaoSepararGreen = self.menuFiltros.addAction( "Separar camada: Verde" )
        self.opcaoSepararGreen.setShortcut( "Ctrl+9" )
        self.opcaoSepararGreen.triggered.connect( self.transform_me9 )

        self.opcaoSepararBlue = self.menuFiltros.addAction( "Separar camada: Azul" )
        self.opcaoSepararBlue.setShortcut( "Ctrl+0" )
        self.opcaoSepararBlue.triggered.connect( self.transform_me0 )
        ##MENU FILTROS TERMINA AQUI ------------------------------------------------------#

        ##MENU TRANSF COMEÇA AQUI ------------------------------------------------------#
        self.opcaLogaritmica = self.menuTransf.addAction( "&Logarítmica" )
        self.opcaLogaritmica.setShortcut( "Ctrl+F1" )
        self.opcaLogaritmica.triggered.connect( self.transform_me11 )#=========================================================================LOGARITIMICA

        self.opcaoSobel = self.menuTransf.addAction( "&Sobel" )
        self.opcaoSobel.setShortcut( "Ctrl+F2" )
        self.opcaoSobel.triggered.connect( self.transform_me12 )#==================================================================================SOBEL

        self.opcaoDeteccao = self.menuTransf.addAction( "&Detecção de Bordas" )
        self.opcaoDeteccao.setShortcut( "Ctrl+F3" )
        self.opcaoDeteccao.triggered.connect( self.transform_me13 )#================================================================================BORDAS

        self.opcaoErosao = self.menuTransf.addAction( "&Erosão" )
        self.opcaoErosao.setShortcut( "Ctrl+F4" )
        self.opcaoErosao.triggered.connect( self.transform_me14 )

        self.opcaoDilatacao = self.menuTransf.addAction( "&Dilatação" )
        self.opcaoDilatacao.setShortcut( "Ctrl+F5" )
        self.opcaoDilatacao.triggered.connect( self.transform_me15 )

        self.opcaoAbertura = self.menuTransf.addAction( "&Abertura" )
        self.opcaoAbertura.setShortcut( "Ctrl+F6" )
        self.opcaoSharpen.triggered.connect( self.transform_me16 )

        self.opcaoFechamento = self.menuTransf.addAction( "&Fechamento" )
        self.opcaoFechamento.setShortcut( "Ctrl+F7" )
        self.opcaoFechamento.triggered.connect( self.transform_me17 )#===============================================================================FECHAMENTO

        #self.opcaoDetBin = self.menuTransf.addAction( "&Detecção Binária" )
        #self.opcaoDetBin.setShortcut( "Ctrl+F8" )
        #self.opcaoSharpen.triggered.connect( self.transform_me18 )

        ##MENU TRANSF TERMINA AQUI ------------------------------------------------------#

        ##MENU SOBRE COMEÇA AQUI ------------------------------------------------------#
        self.opcaosobre = self.menuSobre.addAction("Info Alunos")
        self.opcaosobre.triggered.connect(self.exibe_mensagem)

        self.menuSobre.addSeparator()

        self.opcaosobre2 = self.menuSobre.addAction("Infos Imagem")
        self.opcaosobre2.triggered.connect(self.exibe_mensagem2)
        ##MENU ARQUIVOS TERMINA AQUI ------------------------------------------------------#

        # Criar barra de status
        self.barradestatus = self.statusBar()
        self.barradestatus.showMessage("Oi", 2000)

        # Criando Label
        self.texto = QLabel("Trabalho Final - PDI", self)
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment( QtCore.Qt.AlignCenter )

        # Criando as imagens
        self.imagem1 = QLabel(self)
        self.endereco1 = 'images/narutin.jpg'
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

        self.imagem2 = QLabel(self)
        self.endereco2 = 'images/narutin.jpg'
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
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
            "Data de término do projeto: "
            "\nLink do vídeo: \n"
            "Ituiutaba, Instituto Federal do Triângulo Mineiro")
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
            "Largura:           " 
            "Altura:  ")
        self.msg.setStandardButtons( QMessageBox.Ok | QMessageBox.Cancel )
        self.msg.exec_()  # exibir a caixa de mensagens, ou caixa de diálogo
        self.reply = self.msg.clickedButton()

    def transform_me1(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfNegativo.pgm'
        self.script = 'testeEditor/trabalho01/filtros/filtro_negativo.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap(self.pixmap2)

    def transform_me2(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfGammal.pgm'
        self.script = 'testeEditor/trabalho01/transformacoes/Fator_gama.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )

    def transform_me3(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfSharpen.pgm'
        self.script = 'testeEditor/trabalho01/filtros/sharpen.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )
    
    def transform_me4(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfMediana.pgm'
        self.script = 'testeEditor/trabalho01/filtros/filtro_mediana.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )

    def transform_me5(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfGaussiano.pgm'
        self.script = 'testeEditor/trabalho01/filtros/filtro_gaussiano.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
    
    def transform_me6(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfEscala.pgm'
        self.script = 'testeEditor/trabalho01/filtros/escala_de_cinza.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )

    def transform_me7(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfEscala.pgm'
        self.script = 'testeEditor/trabalho01/filtros/peb.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )
    
    def transform_me8(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfEscala.pgm'
        self.script = 'testeEditor/trabalho01/filtros/filtro_vermelho.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )
    
    def transform_me9(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfEscala.pgm'
        self.script = 'testeEditor/trabalho01/filtros/filtro_verde.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )

    def transform_me0(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfEscala.pgm'
        self.script = 'testeEditor/trabalho01/filtros/filtro_azul.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )



    def transform_me11(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfLog.pgm'
        self.script = 'testeEditor/trabalho01/transformacoes/Transformacao_Logaritmica.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )

    def transform_me12(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfSobel.pgm'
        self.script = 'testeEditor/trabalho01/transformacoes/transfSobel.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )

    def transform_me13(self):
        self.entrada = self.endereco1
        self.saida = 'images/Deteccao_t1.pgm'
        self.script = 'testeEditor/trabalho01/transformacoes/filtro_edge.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )

    def transform_me14(self):
        self.entrada = self.endereco1
        self.saida = 'images/saidaErosao.ppm'
        self.script = 'testeEditor/trabalho01/transformacoes/erosao.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )

    def transform_me15(self):
        self.entrada = self.endereco1
        self.saida = 'images/saidaDilatacao.ppm'
        self.script = 'testeEditor/trabalho01/transformacoes/dilatacao.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )

    def transform_me16(self):
        self.entrada = self.endereco1
        self.saida = 'images/saidaAbertura.pgm'
        self.script = 'testeEditor/trabalho01/transformacoes/abertura.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run( self.program, shell=True )
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap( self.endereco2 )
        self.pixmap2 = self.pixmap2.scaled( 500, 500, QtCore.Qt.KeepAspectRatio )
        self.imagem2.setPixmap( self.pixmap2 )

    def transform_me17(self):
        self.entrada = self.endereco1
        self.saida = 'images/saidaFechamento.pgm'
        self.script = 'testeEditor/trabalho01/transformacoes/fechamento.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print( self.program )
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    


    def open_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName( self, caption='Abrir Imagem',
                                                             directory=QtCore.QDir.currentPath(),
                                                             filter='Todos os Tipos (*);;Images (*.ppm;*.pgm;*.pbm; *.jpg; *.png)',
                                                             initialFilter='Images (*.ppm;*.pgm;*.pbm;*.jpg;*.png;)' )
        if fileName != '':
            self.endereco1 = fileName
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
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

    print(sys.argv + "OI SOU O SYSARGV")


window()

