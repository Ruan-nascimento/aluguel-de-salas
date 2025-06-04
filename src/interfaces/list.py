from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QPushButton, QMessageBox
from utils.list.functions import load_all_reserves, cancel_reserves, conclude_reserves

class ListReserves(QWidget):
    
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(['Nome', 'Sala', 'Data', 'Entrada', 'Saída', 'Total', 'Concluir', 'Cancelar'])
        
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #27272a;
                color: white;
                border: none;
                gridline-color: #3a3a3d;
            }
            QTableWidget::item {
                background-color: #27272a;
                color: white;
            }
            QTableWidget::item:selected {
                background-color: #575757;
                color: white;
            }
            QHeaderView::section {
                background-color: #3f3f46;
                color: white;
                border: none;
                padding: 5px;
            }
            QTableWidget {
                outline: none; 
            }
        """)
        
        self.table.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(self.table.horizontalHeader().Stretch) 
        self.table.verticalHeader().hide()
        
        self.layout.addWidget(self.table)
        self.layout.setContentsMargins(0, 0, 0, 0) 
        self.setLayout(self.layout)
        

        load_all_reserves(self.table, self.conclude_reserve, self.cancel_reserve)
    
    def conclude_reserve(self, i):
        if conclude_reserves(i):
            QMessageBox.warning(self, "Sucesso!", "Reserva Concluída e Removida!")
            load_all_reserves(self.table, self.conclude_reserve, self.cancel_reserve)  
    
    def cancel_reserve(self, i):
        if cancel_reserves(i):
            QMessageBox.warning(self, "Sucesso!", "Reserva Cancelada Com Sucesso...")
            load_all_reserves(self.table, self.conclude_reserve, self.cancel_reserve)