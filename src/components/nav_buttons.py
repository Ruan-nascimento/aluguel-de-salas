from PyQt5.QtWidgets import  QPushButton, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

class Button(QPushButton):
    def __init__(self, text, h='', w=''):
        super().__init__()
        
        # variáveis de inicialização
        self.text = text
        self.h = h
        self.w = w
        
        # definindo o botão
        self.button = QPushButton(text)
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button.setStyleSheet("""
                           QPushButton {
                               background-color: #3A78C2;
                               color: white;
                               outline: none;
                               border-radius: 8px;
                               padding: 10px
                           }
                           
                           QPushButton:hover{
                               background-color: #6AA8F5;
                           }
                           """)
        
        if self.w != '':
            self.button.setFixedWidth(w)
        else:
            self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        if self.h != '':
            self.button.setFixedHeight(h)
        