from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout
from components.calendar import Calendar

class History(QWidget):
    
    def __init__(self):
        super().__init__()
        self.main_layout=QVBoxLayout()
        self.top_layout=QHBoxLayout()
        self.bottom_layout=QVBoxLayout()
        self.innertop_layout=QVBoxLayout()
        self.calendar1=Calendar()
        self.calendar2=Calendar()


        
        self.top_widget=QWidget()
        self.top_widget.setStyleSheet("background-color:#27272A; border-radius: 10px;")
        self.bottom_widget=QWidget()
        self.bottom_widget.setStyleSheet("background-color:#71717A; border-radius: 10px;")
        self.innertop_widget=QWidget()
        self.innertop_widget.setStyleSheet("background-color:#71717A;")
        self.innertop_widget.setFixedWidth(300)
        self.top_widget.setFixedHeight(300)
        


        
        self.top_widget.setLayout(self.top_layout)
        self.bottom_widget.setLayout(self.bottom_layout)
        self.innertop_widget.setLayout(self.innertop_layout)


        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.top_widget)
        self.main_layout.addWidget(self.bottom_widget)
        self.top_layout.addWidget(self.calendar1.calendar)
        self.top_layout.addWidget(self.calendar2.calendar)
        self.top_layout.addWidget(self.innertop_widget)



