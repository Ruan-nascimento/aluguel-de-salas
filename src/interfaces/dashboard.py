from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from utils.fonts import font_bold, font_medium
from components.graphics.data import Datas
from components.graphics.cancel import Cancel_graph
from components.graphics.daily_rentals import Daily_rentals

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
       
        
        # definindo os layouts
        self.main_layout = QVBoxLayout()
        
        self.box_widget = QWidget()
        self.box_widget.setFixedHeight(120)
        self.box_widget.setStyleSheet('background-color: #27272A; border-radius: 10px;')
        self.box_layout = QHBoxLayout()
        
        self.graph_layout = QVBoxLayout()
        
        # layout com gráficos sortidos
        self.graph_layout_1 = QHBoxLayout()
        self.graph_widget_1 = QWidget()
        self.graph_widget_1.setLayout(self.graph_layout_1)
        self.graph_widget_1.setFixedHeight(260)
        
        # layout com gráficos de barra
        self.graph_layout_2 = QHBoxLayout()
        
        
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
        self.graph_datas = Datas().main_widget
        self.graph_cancel = Cancel_graph().main_widget
        self.graph_heatmap = Daily_rentals().main_widget
        
        self.graph_layout_1.addStretch(3)
        self.graph_layout_1.addWidget(self.graph_datas, stretch=1)
        self.graph_layout_1.addWidget(self.graph_cancel, stretch=1)
        self.graph_layout_1.addWidget(self.graph_heatmap, stretch=1)
        self.graph_layout.addWidget(self.graph_widget_1)
        self.graph_layout.addLayout(self.graph_layout_2)
        self.box_widget.setLayout(self.box_layout)
        self.box_layout.addWidget(self.widget_total_value)
        self.box_layout.addWidget(self.widget_total_salas)
        self.box_layout.addWidget(self.widget_total_clientes)
        self.main_layout.addWidget(self.box_widget, stretch=1, alignment=Qt.AlignTop)
        self.main_layout.addLayout(self.graph_layout)
        self.main_layout.addStretch(3)
        self.setLayout(self.main_layout)