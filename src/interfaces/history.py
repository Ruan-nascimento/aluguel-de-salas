from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox, QTableWidget, QTableWidgetItem, QSizePolicy, QHeaderView
from PyQt5.QtCore import Qt
from components.calendar import Calendar
from components.nav_buttons import Button
from utils.fonts import font_medium, font_bold
from datetime import datetime
from utils.files import load_historic

class History(QWidget):
    
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QVBoxLayout()
        self.innertop_layout = QVBoxLayout()
        self.calendar1 = Calendar()
        self.calendar2 = Calendar()
        self.filter_button = Button('Filtrar').button
        self.filter_button.clicked.connect(self.filter)
        self.clear_filter = Button('Limpar Filtro').button
        self.clear_filter.clicked.connect(self.load_historic)
        self.clear_filter.setStyleSheet("""
            QPushButton {
                background-color: #a3a3a3;
                color: white;
                outline: none;
                border-radius: 8px;
                padding: 10px
            }
            QPushButton:hover {
                background-color: #6f6f6f;
            }
        """)
        self.filter_label = QLabel('')
        self.filter_label.setStyleSheet('color: #ffffff')
        self.filter_label.setFont(font_medium)
        
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Nome", "Sala", "Data", "Entrada", "Saída", "Valor"])
        
        self.table.setStyleSheet("""
            QTableWidget {
                color: white; 
                background-color: #3f3f46;
                border: none;
                gridline-color: #71717A;
            }
            QHeaderView::section {
                color: white; 
                background-color: #27272A;
                padding: 5px;
                border: 1px solid #71717A;
            }
            QTableWidget::item {
                border: none;
            }
            QTableWidget::item:selected {
                background-color: #6f6f6f;
                color: white;
            }
            QScrollBar:vertical {
                border: none;
                background: #3f3f46;
                width: 8px; 
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #a3a3a3;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical {
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical {
                height: 0px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }
            QScrollBar:horizontal {
                border: none;
                background: #3f3f46;
                height: 8px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:horizontal {
                background: #a3a3a3;
                min-width: 20px;
                border-radius: 4px;
            }
            QScrollBar::add-line:horizontal {
                width: 0px;
                subcontrol-position: right;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:horizontal {
                width: 0px;
                subcontrol-position: left;
                subcontrol-origin: margin;
            }
            QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
                background: none;
            }
        """)
        
        self.label_not_found = QLabel('')
        self.label_not_found.setFont(font_bold)
        self.label_not_found.setStyleSheet('color: #ffffff;')
        self.label_not_found.hide()  # Inicialmente escondido
        
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.top_widget = QWidget()
        self.top_widget.setStyleSheet("background-color:#27272A; border-radius: 10px;")
        self.bottom_widget = QWidget()
        self.bottom_widget.setStyleSheet("background-color:#71717A; border-radius: 10px;")
        self.innertop_widget = QWidget()
        self.innertop_widget.setStyleSheet("background-color:#3f3f46;")
        self.innertop_widget.setFixedWidth(200)
        self.top_widget.setFixedHeight(300)
        
        self.top_widget.setLayout(self.top_layout)
        self.bottom_widget.setLayout(self.bottom_layout)
        self.innertop_widget.setLayout(self.innertop_layout)
        
        self.setLayout(self.main_layout)
        
        self.main_layout.addWidget(self.top_widget)
        self.main_layout.addWidget(self.bottom_widget, 1)
        self.top_layout.addWidget(self.calendar1)
        self.top_layout.addWidget(self.calendar2)
        self.top_layout.addWidget(self.innertop_widget)
        self.innertop_layout.addWidget(self.filter_label, alignment=Qt.AlignTop)
        self.innertop_layout.addWidget(self.filter_button, alignment=Qt.AlignTop)
        self.innertop_layout.addWidget(self.clear_filter, alignment=Qt.AlignTop)
        self.bottom_layout.addWidget(self.table)
        self.bottom_layout.addWidget(self.label_not_found, alignment=Qt.AlignCenter)  # Adiciona ao layout, mas escondido inicialmente
        
        self.bottom_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_layout.setSpacing(0)
        
        self.table.setMinimumSize(0, 0)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.load_historic()
        
    def load_historic(self):
        historic = load_historic()
        
        # Ordenar por data
        if historic:
            historic = sorted(historic, key=lambda h: datetime.strptime(h['date'], "%d/%m/%Y"), reverse=True)
            
            self.table.setRowCount(len(historic))
            
            for i, h in enumerate(historic):
                self.table.setItem(i, 0, QTableWidgetItem(h['name']))
                self.table.setItem(i, 1, QTableWidgetItem(h['room']))
                self.table.setItem(i, 2, QTableWidgetItem(h['date']))
                self.table.setItem(i, 3, QTableWidgetItem(h['in_hour']))
                self.table.setItem(i, 4, QTableWidgetItem(h['out_hour']))
                self.table.setItem(i, 5, QTableWidgetItem(f"R${h['total_value']:.2f}"))
            
            self.filter_label.setText('')
            self.label_not_found.hide() 
            
        else:
            self.label_not_found.setText('Nenhum Dado Encontrado!')
            self.label_not_found.show() 
                
    def filter(self):
        start = self.calendar1.selectedDate().toString("dd/MM/yyyy")
        start_dt = datetime.strptime(start, "%d/%m/%Y")
        end = self.calendar2.selectedDate().toString("dd/MM/yyyy")
        end_dt = datetime.strptime(end, "%d/%m/%Y")
        
        if end_dt < start_dt:
            QMessageBox.warning(self, 'Erro!', 'A data final deve ser posterior à data inicial!')
            return
        
        self.filter_label.setText(f'De - {start} \n ____________________ \n Até - {end}')
        
        historic = load_historic()
        
        if historic:
            filtered = [h for h in historic if start_dt <= datetime.strptime(h['date'], "%d/%m/%Y") <= end_dt]
            filtered = sorted(filtered, key=lambda h: datetime.strptime(h['date'], "%d/%m/%Y"), reverse=True)
            
            if not filtered:
                self.label_not_found.setText(f'Nenhum Dado Entre {start} --- {end}')
                self.label_not_found.show()
                self.table.setRowCount(0)
            
            else:
                self.table.setRowCount(len(filtered))
                
                for i, h in enumerate(filtered):
                    self.table.setItem(i, 0, QTableWidgetItem(h['name']))
                    self.table.setItem(i, 1, QTableWidgetItem(h['room']))
                    self.table.setItem(i, 2, QTableWidgetItem(h['date']))
                    self.table.setItem(i, 3, QTableWidgetItem(h['in_hour']))
                    self.table.setItem(i, 4, QTableWidgetItem(h['out_hour']))
                    self.table.setItem(i, 5, QTableWidgetItem(f"R${h['total_value']:.2f}"))
                
                self.label_not_found.hide()