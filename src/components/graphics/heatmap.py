from PyQt5.QtWidgets import QWidget, QVBoxLayout

class Heatmap(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setStyleSheet('background-color:#27272A; border-radius: 10px;')
        self.main_widget.setFixedWidth(420)
        self.main_widget.setLayout(self.main_layout)



    