from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd
import json
from utils.files import load_historic  

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
    
    def get_rentals_by_day(self, start_date=None, days=7):

        try:
            historic = load_historic()
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao carregar histórico: {e}")
            return pd.DataFrame({'data': [], 'num_alugueis': []})

        if not historic:
            print("Histórico vazio")
            return pd.DataFrame({'data': [], 'num_alugueis': []})


        if start_date is None:
            start_date = datetime.now() - timedelta(days=days-1)
        end_date = start_date + timedelta(days=days-1)

        data = []
        for r in historic:

            if not isinstance(r, dict) or 'date' not in r:
                print(f"Reserva inválida: {r}")
                continue
            
            try:

                date = datetime.strptime(r['date'], '%d/%m/%Y')

                if start_date <= date <= end_date:
                    data.append({'data': date, 'num_alugueis': 1})
            except ValueError as e:
                print(f"Erro ao processar data de {r}: {e}")
                continue

        df = pd.DataFrame(data)
        if df.empty:
            print("Nenhuma reserva no intervalo de datas")
            return pd.DataFrame({'data': [], 'num_alugueis': []})

        return df

    def graph_bar(self):
        df = self.get_rentals_by_day(days=7)

        if df.empty:
            df = pd.DataFrame({
                'data': [datetime.now() - timedelta(days=i) for i in range(6, -1, -1)],
                'num_alugueis': [0] * 7
            })

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