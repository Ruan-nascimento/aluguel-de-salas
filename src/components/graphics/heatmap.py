from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import json
from datetime import datetime
from utils.files import load_historic  

class Heatmap(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setStyleSheet('background-color:#27272A; border-radius: 10px; border: 1px solid #F97316;')
        self.main_widget.setLayout(self.main_layout)

        self.months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

        self.create_heatmap()

    def get_values_by_month(self, year=None):

        try:
            historic = load_historic()
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao carregar histórico: {e}")
            return [0.0] * 12 

        if year is None:
            year = datetime.now().year

        monthly_totals = {i: 0.0 for i in range(1, 13)}

        if historic:
            for r in historic:
                if not isinstance(r, dict) or 'date' not in r or 'total_value' not in r:
                    print(f"Reserva inválida: {r}")
                    continue
                
                try:

                    date = datetime.strptime(r['date'], '%d/%m/%Y')

                    if date.year == year:
                        value = float(r['total_value']) 
                        month = date.month
                        monthly_totals[month] += value
                except (ValueError, TypeError) as e:
                    print(f"Erro ao processar reserva {r}: {e}")
                    continue

        values = [monthly_totals[i] for i in range(1, 13)]
        return values

    def create_heatmap(self):

        values = self.get_values_by_month()
        values = np.array(values) 

        # Cria o gráfico
        fig, ax = plt.subplots(figsize=(4, 4))
        fig.set_facecolor('#333333')
        ax.set_facecolor('#444444')

        ax.plot(self.months, values, marker='o', color='#F97316', label='Valor R$ por Mês')


        for i, value in enumerate(values):
            ax.text(i, value + 5, f'R$ {value:.2f}'.replace('.', ','), ha='center', va='bottom', color='white') 

        ax.set_title('Valores por Mês do Ano', fontsize=14, pad=20, color='white') 
        ax.set_xlabel('Mês', fontsize=12, color='white')
        ax.set_ylabel('Valor (R$)', fontsize=12, color='white')  
        ax.grid(True, linestyle='--', alpha=0.7, color='gray') 
        ax.legend(facecolor='#333333', edgecolor='#F97316', labelcolor='white') 

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        ax.set_ylim(min(values) - 20 if values.any() else -20, max(values) + 40 if values.any() else 40)

        canvas = FigureCanvas(fig)
        self.main_layout.addWidget(canvas)

        plt.close(fig)