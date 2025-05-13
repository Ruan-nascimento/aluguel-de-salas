from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from utils.fonts import font_datas

class Cancel_graph(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setStyleSheet('background-color:#27272A; border-radius: 10px; border: 1px solid #F97316;')
        self.main_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.main_widget.setLayout(self.main_layout)
        
        # texto
        self.label = QLabel('Porcentagem de Cancelamento')
        self.label.setFont(font_datas)
        self.label.setStyleSheet('color: #ffffff; border: transparent;')

        # adicionando label
        self.main_layout.addWidget(self.label, alignment=Qt.AlignCenter)
        
        # Criar o gráfico de rosca
        self.create_chart()
        

    def create_chart(self):
        cancel = 11.67
        completed = 100 - cancel
        sizes = [cancel, completed]
        colors = ['#c12320', '#59c130'] 

        fig, ax = plt.subplots(facecolor='#27272A', figsize=(5,5) )
        ax.set_facecolor('#27272A')

        wedges, texts = ax.pie(sizes, labels=None, colors=colors, startangle=90,
                               wedgeprops=dict(width=0.4, edgecolor='none'))

        ax.text(0, 0, f'{cancel}%', 
                ha='center', va='center', fontsize=14, color='white', weight='bold')
        
        ax.axis('equal') 

        canvas = FigureCanvas(fig)
        self.main_layout.addWidget(canvas)

        plt.close(fig)