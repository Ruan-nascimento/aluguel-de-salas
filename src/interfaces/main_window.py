from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QVBoxLayout, QStackedWidget, QSpacerItem, QSizePolicy, QLabel
from interfaces.new_reserve import NewReserve
from interfaces.list import ListReserves
from interfaces.history import History
from interfaces.managment import Managment
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
                               background-color: #27272A;
                               }
                           """)
        
        # widget principal
        self.central_widget = QWidget()
        
        # layout principal 
        self.main_layout = QHBoxLayout()
        
        # layouts de navegação
        self.nav_widget = QWidget()
        self.nav_widget.setStyleSheet('background-color: #3F3F46;')
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
        self.pages.setStyleSheet('background-color: #3F3F46;')
        
        # adicionando as páginas
        self.page_new_reserve = NewReserve()
        self.page_list_reserves = ListReserves()
        self.page_managment = Managment()
        self.page_history = History()
        
        self.pages.addWidget(self.page_new_reserve)
        self.pages.addWidget(self.page_managment)
        self.pages.addWidget(self.page_list_reserves)
        self.pages.addWidget(self.page_history)
        
        # Definição do layout central e widget central
        self.nav_widget.setLayout(self.nav_layout)
        self.main_layout.addWidget(self.nav_widget)
        self.main_layout.addWidget(self.pages)
        
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        
        # execução de funções
        self.get_current_page()
        
        
    # função para abrir a página de Adicionar nova reserva
    def new_reserve(self):
        self.pages.setCurrentWidget(self.page_new_reserve)
        self.get_current_page()
    
    # função para abrir a página de reservas
    def open_reserves(self):
        self.pages.setCurrentWidget(self.page_list_reserves)
        self.get_current_page()
    
    # função para abrir página de gerenciamento de salas 
    def managment(self):
        self.pages.setCurrentWidget(self.page_managment)
        self.get_current_page()
    
    # função para abrir página de histórico
    def history(self):
        self.pages.setCurrentWidget(self.page_history)
        self.get_current_page()
    
    # função para reconhecer a página atual
    def get_current_page(self):
        current = self.pages.currentWidget()
        
        pages = {
            self.page_history: self.button_history,
            self.page_list_reserves: self.button_reserve,
            self.page_managment: self.button_managment,
            self.page_new_reserve: self.button_new_reserve
        }
        
        for k, v in pages.items():
            if current == k:
                v.button.setStyleSheet("""
                                       QPushButton {
                                        background-color: #C2410C;
                                        color: white;
                                        outline: none;
                                        border-radius: 8px;
                                        padding: 10px
                                    }
                           
                                        QPushButton:hover{
                                            background-color: #8f2f08;
                                        }
                                       """)
            
            else:
                v.button.setStyleSheet("""
                                       QPushButton {
                                        background-color: #F97316;
                                        color: white;
                                        outline: none;
                                        border-radius: 8px;
                                        padding: 10px
                                    }
                           
                                        QPushButton:hover{
                                            background-color: #c55b11;
                                        }
                                       """)
        