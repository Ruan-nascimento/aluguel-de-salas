from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QVBoxLayout, QStackedWidget, QSpacerItem, QSizePolicy, QLabel
from components.nav_buttons import Button
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # configurações iniciais da tela
        self.setFixedSize(1280, 720)
        self.setWindowTitle('Aluguel de Salas')
        
        # icone da janela
        icon_path = os.path.join(os.path.dirname(__file__), '../../assets/logo_principal.ico')
        self.icon = QIcon(icon_path)
        
        # verificação se o icone é válido
        if self.icon.isNull():
            print(f'Erro icone selecionado inexistente ou caminho inválido - {icon_path}')
        else:
            self.setWindowIcon(self.icon)
        
        # Estilização 
        self.setStyleSheet("""
                           QMainWindow {
                               background-color: #8A9A97;
                           }
                           """)
        
        # widget principal
        self.central_widget = QWidget()
        
        # layout principal 
        self.main_layout = QHBoxLayout()
        
        # layouts de navegação
        self.nav_widget = QWidget()
        self.nav_widget.setStyleSheet('background-color: #6B7E7A;')
        self.nav_widget.setFixedWidth(250)
        self.nav_layout = QVBoxLayout()
        self.nav_layout.setAlignment(Qt.AlignHCenter)
        self.nav_layout.setSpacing(15)
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # definindo imagem
        logo_path = os.path.join(os.path.dirname(__file__), '../../assets/logo.png')
        self.logo = QLabel(self)
        self.pixmap = QPixmap(logo_path)
        
        # verificando se a logo existe se está válida
        if self.pixmap.isNull():
            print(f'Erro {logo_path}')
        else:
            self.pixmap = self.pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.logo.setPixmap(self.pixmap)
            self.logo.setAlignment(Qt.AlignCenter)
            self.logo.setStyleSheet('margin-bottom: 30px;')
            
        
        #  botões de navegação
        self.button_new_reserve = Button('Nova Reserva')
        self.button_new_reserve.button.clicked.connect(self.new_reserve)
        
        self.button_reserve = Button('Reservas')
        self.button_reserve.button.clicked.connect(self.open_reserves)
        
        self.button_managment = Button('Gerenciar Salas')
        self.button_managment.button.clicked.connect(self.managment)
        
        self.button_history = Button('Histórico')
        self.button_history.button.clicked.connect(self.history)
        
        # definindo botões no layout de navegação
        self.nav_layout.addWidget(self.logo)
        self.nav_layout.addWidget(self.button_new_reserve.button)
        self.nav_layout.addWidget(self.button_reserve.button)
        self.nav_layout.addWidget(self.button_managment.button)
        self.nav_layout.addWidget(self.button_history.button)
        
        # definindo o spacer no layout
        self.nav_layout.addSpacerItem(spacer)
        
        # páginas e sistema de paginação
        self.pages = QStackedWidget()
        self.pages.setStyleSheet('background-color: #6B7E7A;')
        
        # Definição do layout central e widget central
        self.nav_widget.setLayout(self.nav_layout)
        self.main_layout.addWidget(self.nav_widget)
        self.main_layout.addWidget(self.pages)
        
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        
        
    # função para abrir a página de Adicionar nova reserva
    def new_reserve(self):
        print(self.button_new_reserve.text)
    
    # função para abrir a página de reservas
    def open_reserves(self):
        print(self.button_reserve.text)
    
    # função para abrir página de gerenciamento de salas 
    def managment(self):
        print(self.button_managment.text)
    
    # função para abrir página de histórico
    def history(self):
        print(self.button_history.text)