from PyQt5.QtWidgets import QWidget, QVBoxLayout

class Mount_payment(QWidget):
    def __init__(self):
        super().__init__()
        
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setStyleSheet('background-color:#27272A; border-radius:10px; border: 1px solid #F97316;')
        self.main_widget.setFixedWidth(480)
        self.main_widget.setLayout(self.main_layout)