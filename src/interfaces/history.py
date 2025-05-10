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
        self.top_widget.setStyleSheet("background-color:#092358;")
        self.bottom_widget=QWidget()
        self.bottom_widget.setStyleSheet("background-color:#456710;")
        self.innertop_widget=QWidget()
        self.innertop_widget.setStyleSheet("background-color:#780304;")
        self.innertop_widget.setFixedSize(100, 100)
        self.top_widget.setFixedHeight(200)
        


        
        self.top_widget.setLayout(self.top_layout)
        self.bottom_widget.setLayout(self.bottom_layout)
        self.innertop_widget.setLayout(self.innertop_layout)


        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.top_widget)
        self.main_layout.addWidget(self.bottom_widget)
        self.top_layout.addWidget(self.calendar1)
        self.top_layout.addWidget(self.calendar2)
        self.top_layout.addWidget(self.innertop_widget)



