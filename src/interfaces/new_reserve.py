from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox
from PyQt5.QtCore import Qt
from utils.fonts import font_title
from components.calendar import Calendar
from components.nav_buttons import Button
from utils.new_reserve.functions import update_rooms, create_reserve

class NewReserve(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("""
                           QMessageBox {
                               background-color: #27272A;
                               color: #ffffff
                           }
                           
                           QLabel {
                               color: #ffffff;
                               font-size: 20px;
                           }
                           
                           QLineEdit {
                                background-color: #27272A;
                                color: #ffffff;
                                border: 2px solid #F97316; 
                                border-radius: 5px;
                                padding: 5px;
                                font-size: 14px; 
                           }
                           
                           QComboBox {
                                background-color: #27272A;
                                color: #ffffff;
                                border: 2px solid #F97316; 
                                border-radius: 5px;
                                padding: 5px;
                                font-size: 18px;
                            }
                            QComboBox::drop-down {
                                border: none;
                                width: 20px;
                            }
                            QComboBox::down-arrow {
                                image: url(assets/arrowdown.png);
                                width: 12px;
                                height: 12px;
                            }
                            QComboBox QAbstractItemView {
                                background-color: #3F3F46;
                                color: #ffffff;
                                border-radius: 10px;
                                selection-background-color: #C2410C;
                                selection-color: #ffffff;
                                border: 1px solid #F97316;
                            }
                           """)
        
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        
        self.title = QLabel('Criar Nova Reserva')
        self.title.setFont(font_title)
        self.title.setStyleSheet('color: #ffffff; font-size: 24px;')
        self.main_layout.addWidget(self.title, alignment=Qt.AlignCenter)
        
        self.layout_widgets = QHBoxLayout()
        self.widget_widgets = QWidget()
        self.widget_widgets.setFixedHeight(600)
        self.widget_widgets.setStyleSheet('background-color: #27272A; border-radius: 10px;')
        self.widget_widgets.setLayout(self.layout_widgets)
                
        
        self.form_layout = QVBoxLayout()
        self.form_widget = QWidget()
        self.form_widget.setLayout(self.form_layout)
        self.form_widget.setFixedWidth(500)
        self.form_widget.setFixedHeight(500)
        
        # widgets do formulario
        self.name = QLabel('Nome')
        self.input_name = QLineEdit()
        self.input_name.setStyleSheet("padding: 10px;")
        self.input_name.setPlaceholderText('Digite o Nome')
        self.salas_lbl = QLabel('Lista de Salas')
        self.salas = QComboBox()
        self.entrada = QLabel('Horário de Entrada')
        self.entrada_box = QComboBox()
        self.saida = QLabel('Horário de Saída')
        self.saida_box = QComboBox()
        
        self.reservar = Button('Reservar').button
        self.reservar.clicked.connect(self.create_new_reserve)
        self.limpar = Button('Limpar').button
        self.limpar.clicked.connect(self.clear_fields)
        self.limpar.setStyleSheet("""
                                       QPushButton {
                                        background-color: #d8d8d8;
                                        color: #000000;
                                        outline: none;
                                        border-radius: 8px;
                                        padding: 10px
                                    }
                           
                                        QPushButton:hover{
                                            background-color: #8b8b8b;
                                        }
                                       """)
        
        horarios = [f"{h:02d}:00" for h in range(8,23)]
        self.entrada_box.addItems(horarios)
        self.saida_box.addItems(horarios)
        
        # adicionando items do formulario ao layout
        self.form_layout.addWidget(self.name)
        self.form_layout.addWidget(self.input_name)
        self.form_layout.addWidget(self.salas_lbl)
        self.form_layout.addWidget(self.salas)
        self.form_layout.addWidget(self.entrada)
        self.form_layout.addWidget(self.entrada_box)
        self.form_layout.addWidget(self.saida)
        self.form_layout.addWidget(self.saida_box)
        self.form_layout.addSpacing(30)
        self.form_layout.addWidget(self.reservar)
        self.form_layout.addSpacing(10)
        self.form_layout.addWidget(self.limpar)
        
        
        self.calendar_layout = QVBoxLayout()
        self.calendar_widget = QWidget()
        self.calendar_widget.setLayout(self.calendar_layout)
        self.calendar_widget.setFixedWidth(450)
        self.calendar_widget.setStyleSheet('background-color: #27272A;')
        
       
        self.calendar = Calendar()
        self.calendar_layout.addWidget(self.calendar)
        
        self.layout_widgets.addWidget(self.form_widget, alignment=Qt.AlignTop)
        self.layout_widgets.addWidget(self.calendar_widget, alignment=Qt.AlignLeft)
        
        self.main_layout.addWidget(self.widget_widgets)
        self.setLayout(self.main_layout)
        
        self.load_rooms()
        
        
    def clear_fields(self):
        self.input_name.setText('')
        self.entrada_box.setCurrentIndex(0)
        self.saida_box.setCurrentIndex(0)
    
    def load_rooms(self):
        update = update_rooms()
        if update == True:
            QMessageBox.warning(self, "Falha na Busca", "A Aplicação Não Conseguiu Encontrar o Banco de Salas")
        
        else:
            self.salas.clear()
            self.salas.addItems(update_rooms())
    
    def create_new_reserve(self):
        name = self.input_name.text()
        room = self.salas.currentText()
        date = self.calendar.selectedDate().toString("dd/MM/yyyy")
        in_hour = self.entrada_box.currentText()
        out_hour = self.saida_box.currentText()
        
        if name and room:
            success, message = create_reserve(name, room, date, in_hour, out_hour)
            
            if success:
                QMessageBox.warning(self, "Sucesso", message)
                self.input_name.clear()
                self.entrada_box.setCurrentIndex(0)
                self.saida_box.setCurrentIndex(0)
            
            else:
                QMessageBox.warning(self, "Erro!", message)
        
        else:
            QMessageBox.warning(self, "Não é Possivel!", "Preencha Todos os Campos!!!")
    
    