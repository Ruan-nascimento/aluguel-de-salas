from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QDoubleSpinBox, QTableWidget, QTableWidgetItem, QMessageBox, QLabel, QPushButton)
from PyQt5.QtCore import Qt
from utils.files import load_rooms
from utils.rooms.functions import add_room, remove_room
from components.nav_buttons import Button

class Managment(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciamento das Salas")
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)  # Alinha tudo ao topo

        # Título
        self.titulo = QLabel("Gerenciamento das Salas")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet("font-size: 24px; color: #ffffff; font-weight: bold;")
        self.titulo.setFixedHeight(40)
        self.layout.addWidget(self.titulo)

        self.main_layout = QHBoxLayout()
        self.main_layout.setAlignment(Qt.AlignTop)  # Alinha as seções ao topo

        # Área de Criar Nova Sala (esquerda)
        self.criar_layout = QVBoxLayout()
        self.criar_layout.setAlignment(Qt.AlignTop)  # Alinha os elementos ao topo
        self.criar_label = QLabel("Criar Nova Sala")
        self.criar_label.setStyleSheet("font-size: 16px; color: #ffffff; margin-bottom: 5px;")
        self.criar_label.setFixedHeight(30)
        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Nome da Sala")
        self.nome_input.setStyleSheet("background-color: #27272a; color: white; border: 1px solid #f4a261; border-radius: 5px; padding: 5px; font-size: 14px; margin-bottom: 10px;")
        self.valor_label = QLabel("Valor Por Hora R$")
        self.valor_label.setStyleSheet("color: #ffffff; font-size: 14px; margin-bottom: 5px;")
        self.valor_label.setFixedHeight(30)
        self.valor_input = QDoubleSpinBox()
        self.valor_input.setRange(0, 1000)
        self.valor_input.setPrefix("R$ ")
        self.valor_input.setStyleSheet("background-color: #27272a; color: white; border: 1px solid #f4a261; border-radius: 5px; padding: 5px; font-size: 14px; margin-bottom: 10px;")
        self.botao_salvar = Button('Salvar Sala').button
        self.botao_limpar = Button('Limpar').button
        self.botao_limpar.setStyleSheet("""
                                       QPushButton {
                                        background-color: #a3a3a3;
                                        color: white;
                                        outline: none;
                                        border-radius: 8px;
                                        padding: 10px
                                    }
                           
                                        QPushButton:hover{
                                            background-color: #6f6f6f;
                                        }
                                       """)
        self.botao_salvar.clicked.connect(self.adicionar_sala)
        self.botao_limpar.clicked.connect(self.limpar_campos)
        self.criar_layout.addWidget(self.criar_label)
        self.criar_layout.addWidget(self.nome_input)
        self.criar_layout.addWidget(self.valor_label)
        self.criar_layout.addWidget(self.valor_input)
        self.botao_layout = QHBoxLayout()
        self.botao_layout.setAlignment(Qt.AlignTop)  # Alinha os botões ao topo
        self.botao_layout.addWidget(self.botao_salvar)
        self.botao_layout.addWidget(self.botao_limpar)
        self.criar_layout.addLayout(self.botao_layout)

        # Área de Listagem de Salas (direita, agora com tabela)
        self.salas_layout = QVBoxLayout()
        self.salas_layout.setAlignment(Qt.AlignTop)  # Alinha os elementos ao topo
        self.salas_label = QLabel("Salas Disponíveis")
        self.salas_label.setStyleSheet("font-size: 16px; color: #ffffff; margin-bottom: 5px;")
        self.salas_label.setFixedHeight(30)

        # Tabela de salas
        self.salas_table = QTableWidget()
        self.salas_table.setColumnCount(4)
        self.salas_table.setHorizontalHeaderLabels(['Nome', 'Valor Por Hora', 'Editar', 'Remover'])
        self.salas_table.setStyleSheet("""
            QTableWidget {
                background-color: #27272a;
                color: white;
                border: 1px solid #f4a261;
                font-size: 14px;
            }
            QTableWidget::item {
                background-color: #27272a;
                color: white;
                padding: 5px;
            }
            QTableWidget::item:selected {
                background-color: #3f3f46;
                color: white;
            }
            QHeaderView::section {
                background-color: #3f3f46;
                color: #f4a261;
                border: 1px solid #f4a261;
                padding: 5px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #27272a;
                color: #f4a261;
                border: 1px solid #f4a261;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
                min-height: 30px;  # Aumenta a altura dos botões
            }
            QPushButton:hover {
                background-color: #3f3f46;
            }
        """)
        self.salas_table.horizontalHeader().setStretchLastSection(True)
        self.salas_table.horizontalHeader().setSectionResizeMode(self.salas_table.horizontalHeader().Stretch)
        self.salas_table.verticalHeader().hide()

        self.salas_layout.addWidget(self.salas_label)
        self.salas_layout.addWidget(self.salas_table)

        # Adicionar layouts ao layout principal com pesos iguais (50% cada)
        self.main_layout.addLayout(self.criar_layout, 1)
        self.main_layout.addLayout(self.salas_layout, 1)
        self.layout.addLayout(self.main_layout)

        # Estilizar o widget principal
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(10)
        self.setLayout(self.layout)

        self.carregar_salas()

    def carregar_salas(self):
        self.salas_table.setRowCount(0)
        rooms = load_rooms()
        if rooms:
            self.salas_table.setRowCount(len(rooms))
            for i, room in enumerate(rooms):
                self.salas_table.setItem(i, 0, QTableWidgetItem(room['name']))
                self.salas_table.setItem(i, 1, QTableWidgetItem(f"R$ {room['value']:.2f} /h"))
                editar_btn = Button('Edit').button
                editar_btn.setStyleSheet("""
                                       QPushButton {
                                        background-color: #a3a3a3;
                                        color: white;
                                        outline: none;
                                        border-radius: 8px;
                                        padding: 10px
                                    }
                           
                                        QPushButton:hover{
                                            background-color: #6f6f6f;
                                        }
                                       """)
                remover_btn = Button('X').button
                remover_btn.setStyleSheet("""
                                       QPushButton {
                                        background-color: #7a0012;
                                        color: white;
                                        outline: none;
                                        border-radius: 8px;
                                        padding: 10px
                                    }
                           
                                        QPushButton:hover{
                                            background-color: #5c0512;
                                        }
                                       """)
                remover_btn.clicked.connect(lambda checked, nome=room['name']: self.remover_sala(nome))
                self.salas_table.setCellWidget(i, 2, editar_btn)
                self.salas_table.setCellWidget(i, 3, remover_btn)
        else:
            self.salas_table.setRowCount(1)
            self.salas_table.setItem(0, 0, QTableWidgetItem('Nenhuma Sala Disponível'))
            self.salas_table.setItem(0, 1, QTableWidgetItem(''))
            self.salas_table.setCellWidget(0, 2, None)
            self.salas_table.setCellWidget(0, 3, None)

    def adicionar_sala(self):
        nome = self.nome_input.text()
        valor_hora = self.valor_input.value()
        if nome and valor_hora:
            if add_room(nome, valor_hora):
                QMessageBox.information(self, "Sucesso", "Nova Sala Criada!")
                self.limpar_campos()
                self.carregar_salas()
            else:
                QMessageBox.warning(self, "Erro", "Sala já existe!")
        else:
            QMessageBox.warning(self, "Erro", "Preencha os campos para prosseguir!")

    def remover_sala(self, nome):
        if nome:
            sucesso, mensagem = remove_room(nome)
            if sucesso:
                QMessageBox.information(self, "Sucesso", mensagem)
                self.carregar_salas()
            else:
                QMessageBox.warning(self, "Erro", mensagem)
        else:
            QMessageBox.warning(self, "Erro", "Selecione uma sala para remover!")

    def limpar_campos(self):
        self.nome_input.clear()
        self.valor_input.setValue(0)