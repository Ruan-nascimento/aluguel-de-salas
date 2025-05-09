from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from utils.fonts import font_bold, font_medium
from utils.dashboard_functions import plot

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
       
        
        # definindo os layouts
        self.main_layout = QVBoxLayout()
        
        self.box_widget = QWidget()
        self.box_widget.setFixedHeight(120)
        self.box_widget.setStyleSheet('background-color: #27272A; border-radius: 10px;')
        self.box_layout = QHBoxLayout()
        
        # gráfico
        self.graph_widget = QWidget()
        self.graph_widget.setStyleSheet('border-radius: 10px;')
        self.graph_layout = QHBoxLayout()
        self.graph_widget.setLayout(self.graph_layout)
        self.graph = plot(self.graph_layout)
        
        
        # box 1 - valor total
        self.widget_total_value = QWidget()
        self.widget_total_value.setFixedHeight(100)
        self.widget_total_value.setStyleSheet('background-color: #3F3F46; border-radius: 10px;')
        self.box_total_value = QVBoxLayout()
        self.valor = QLabel('R$ 144,50')
        self.valor.setFont(font_bold)
        self.valor.setStyleSheet('color: #F97316;')
        self.label_1 = QLabel('Valor Total')
        self.label_1.setFont(font_medium)
        self.label_1.setStyleSheet('color: #ffffff')

        
        self.widget_total_value.setLayout(self.box_total_value)
        self.box_total_value.addWidget(self.label_1)
        self.box_total_value.addWidget(self.valor)
        
        # box 2 - Total de Salas alugadas
        self.widget_total_salas = QWidget()
        self.widget_total_salas.setFixedHeight(100)
        self.widget_total_salas.setStyleSheet('background-color: #3F3F46; border-radius: 10px;')
        self.box_total_salas = QVBoxLayout()
        self.salas = QLabel('4')
        self.salas.setFont(font_bold)
        self.salas.setStyleSheet('color: #F97316;')
        self.label_2 = QLabel('Salas Alugadas')
        self.label_2.setFont(font_medium)
        self.label_2.setStyleSheet('color: #ffffff')

        self.widget_total_salas.setLayout(self.box_total_salas)
        self.box_total_salas.addWidget(self.salas)
        self.box_total_salas.addWidget(self.label_2)
        
        # box 3 - Total de Clientes
        self.widget_total_clientes = QWidget()
        self.widget_total_clientes.setFixedHeight(100)
        self.widget_total_clientes.setStyleSheet('background-color: #3F3F46; border-radius: 10px;')
        self.box_total_clientes = QVBoxLayout()
        self.clientes = QLabel('12')
        self.clientes.setFont(font_bold)
        self.clientes.setStyleSheet('color: #F97316;')
        self.label_3 = QLabel('Total de Clientes')
        self.label_3.setFont(font_medium)
        self.label_3.setStyleSheet('color: #ffffff')

        self.widget_total_clientes.setLayout(self.box_total_clientes)
        self.box_total_clientes.addWidget(self.clientes)
        self.box_total_clientes.addWidget(self.label_3)
        
        
        # setando configurações
        self.box_widget.setLayout(self.box_layout)
        self.box_layout.addWidget(self.widget_total_value)
        self.box_layout.addWidget(self.widget_total_salas)
        self.box_layout.addWidget(self.widget_total_clientes)
        self.main_layout.addWidget(self.box_widget, stretch=1, alignment=Qt.AlignTop)
        self.main_layout.addWidget(self.graph_widget)
        self.main_layout.addStretch(3)
        self.setLayout(self.main_layout)