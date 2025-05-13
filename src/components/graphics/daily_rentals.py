from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime, timedelta
import pandas as pd
import random

class Daily_rentals(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setStyleSheet('background-color:#27272A; border-radius: 10px; border: 1px solid #F97316;')
        self.main_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.main_widget.setFixedWidth(420)
        self.main_widget.setLayout(self.main_layout)
        
        self.graph_bar()

    def graph_bar(self):
        data = []
        start_date = datetime(2025, 5, 5)
        for i in range(7):
            dia = start_date + timedelta(days=i)
            num_alugueis = random.randint(5, 20)
            data.append({
                'data': dia,
                'num_alugueis': num_alugueis
            })
        df = pd.DataFrame(data)

        df['dia_semana'] = df['data'].dt.day_name()

        dias_map = {
            'Monday': 'SE', 
            'Tuesday': 'TE',
            'Wednesday': 'QT',
            'Thursday': 'QN', 
            'Friday': 'SX',  
            'Saturday': 'SB',
            'Sunday': 'DM'  
        }
        df['dia_semana'] = df['dia_semana'].map(dias_map)

     
        df_grouped = df.groupby('dia_semana')['num_alugueis'].sum().reset_index()


        ordem_dias = ['DM', 'SE', 'TE', 'QT', 'QN', 'SX', 'SB']
        df_grouped = df_grouped.set_index('dia_semana').reindex(ordem_dias).reset_index().fillna(0)

    
        fig, ax = plt.subplots(figsize=(6, 3), facecolor='#27272A')
        ax.set_facecolor('#27272A')
        ax.grid(linestyle='--', linewidth=0.5, axis='y')


        ax.bar(df_grouped['dia_semana'], df_grouped['num_alugueis'], color='#F97316', edgecolor='none', width=0.4)


        ax.set_title('Aluguéis Por Dia', color='#F97316', fontsize=8)
        ax.set_xlabel('Dia da Semana', color='#F97316', fontsize=8)
        ax.set_ylabel('Quantidade de Aluguéis', color='#F97316', fontsize=8)
        ax.tick_params(colors='white')


        plt.tight_layout()


        canvas = FigureCanvas(fig)
        canvas.setFixedWidth(370)
        self.main_layout.addWidget(canvas, alignment=Qt.AlignCenter)

        plt.close(fig)

    