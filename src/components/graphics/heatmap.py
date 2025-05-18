from PyQt5.QtWidgets import QWidget, QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class Heatmap(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setStyleSheet('background-color:#27272A; border-radius: 10px; border: 1px solid #F97316;')
        self.main_widget.setLayout(self.main_layout)

        self.months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        self.values = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

        self.create_heatmap()

    def create_heatmap(self):
        fig, ax = plt.subplots(figsize=(4, 4))

        fig.set_facecolor('#333333')
        ax.set_facecolor('#444444')

        ax.plot(self.months, self.values, marker='o', color='#F97316', label='Valor R$ por Mês')

        for i, value in enumerate(self.values):
            ax.text(i, value + 5, f'{value}', ha='center', va='bottom', color='white') 

        ax.set_title('Valores por Mês do Ano', fontsize=14, pad=20, color='white') 
        ax.set_xlabel('Mês', fontsize=12, color='white')
        ax.set_ylabel('Valor', fontsize=12, color='white')  
        ax.grid(True, linestyle='--', alpha=0.7, color='gray') 
        ax.legend(facecolor='#333333', edgecolor='#F97316', labelcolor='white') 

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        ax.set_ylim(min(self.values) - 20, max(self.values) + 40)

        canvas = FigureCanvas(fig)
        self.main_layout.addWidget(canvas)