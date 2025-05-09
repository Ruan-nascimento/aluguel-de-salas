from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from datetime import datetime
import json
import os

def plot(graph_layout):
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "../services/clients.json")
    with open(json_path, 'r') as f:
            clientes = json.load(f)
    
    figure, ax = plt.subplots()
    canvas = FigureCanvas(figure)
    graph_layout.addWidget(canvas)
    
    months = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", 
          "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    
    month_counts = Counter(datetime.strptime(client['entry_date'], "%Y-%m-%d").month for client in clientes)
    values = [month_counts.get(i, 0) for i in range(1,13)]
    

    x = np.arange(len(months))
    bars = ax.bar(x, values, color='#F97316')
    ax.set_xticks(x)
    ax.grid(True, color='white', linestyle=':', linewidth=0.8, alpha=1, axis='y')
    ax.set_xticklabels(months, rotation=0)
    ax.set_title('Clientes Por Mês', color='white', fontsize=12)
    ax.set_facecolor('#27272A')
    figure.set_facecolor('#27272A')
    ax.tick_params(colors='#ffffff')
    ax.spines['bottom'].set_color('gray')
    ax.spines['top'].set_color('gray')
    ax.spines['left'].set_color('gray')
    ax.spines['right'].set_color('gray')
    