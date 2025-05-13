from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from utils.fonts import font_datas_value, font_datas
from PyQt5.QtCore import Qt

class Datas(QWidget):
    def __init__(self):
        super().__init__()
        
        # definindo layouts e widgets
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.main_widget.setStyleSheet('background-color: #27272A; border-radius: 10px;')
        
        # alugueis concluidos
        self.total_aluguel = QWidget()
        self.total_aluguel_layout = QVBoxLayout()
        self.total_aluguel.setLayout(self.total_aluguel_layout)
        self.total_aluguel.setStyleSheet('background-color: #3F3F46; color: #ffffff; border-radius: 10px;')
        
        self.label_1 = QLabel('Total de Aluguéis Concluidos')
        self.label_1.setFont(font_datas)
        self.label_2 = QLabel('68')
        self.label_2.setStyleSheet('color: #F97316;')
        self.label_2.setFont(font_datas_value)
        
        self.total_aluguel_layout.addWidget(self.label_1)
        self.total_aluguel_layout.addWidget(self.label_2, alignment=Qt.AlignCenter)
        
        # Faturamento total
        self.total_faturamento = QWidget()
        self.total_faturamento_layout = QVBoxLayout()
        self.total_faturamento.setLayout(self.total_faturamento_layout)
        self.total_faturamento.setStyleSheet('background-color: #3F3F46; color: #ffffff; border-radius: 10px;')
        
        self.label_3 = QLabel('Faturamento Total')
        self.label_3.setFont(font_datas)
        self.label_4 = QLabel('R$ 1.239,00')
        self.label_4.setStyleSheet('color: #008000;')
        self.label_4.setFont(font_datas_value)
        
        self.total_faturamento_layout.addWidget(self.label_3)
        self.total_faturamento_layout.addWidget(self.label_4)
        
        # total de cancelamentos
        self.total_cancelamento = QWidget()
        self.total_cancelamento_layout = QVBoxLayout()
        self.total_cancelamento.setLayout(self.total_cancelamento_layout)
        self.total_cancelamento.setStyleSheet('background-color: #3F3F46; color: #ffffff; border-radius: 10px;')
        
        self.label_5 = QLabel('Total de Cancelamentos')
        self.label_5.setFont(font_datas)
        self.label_6 = QLabel('23')
        self.label_6.setStyleSheet('color: #F97316;')
        self.label_6.setFont(font_datas_value)
        
        self.total_cancelamento_layout.addWidget(self.label_5)
        self.total_cancelamento_layout.addWidget(self.label_6, alignment=Qt.AlignCenter)

        
        
        

        
        # definições finais
        self.main_layout.addWidget(self.total_faturamento)
        self.main_layout.addWidget(self.total_aluguel)
        self.main_layout.addWidget(self.total_cancelamento)
        