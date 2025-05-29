from PyQt5.QtWidgets import QCalendarWidget
from PyQt5.QtGui import QTextCharFormat, QColor, QFont
from PyQt5.QtCore import Qt, QDate

class Calendar(QCalendarWidget):
    def __init__(self):
        super().__init__()

        self.setGridVisible(True)
        self.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        self.setStyleSheet("""
            QCalendarWidget QWidget {
                background-color: #27272A;
                color: white;
            }

            QCalendarWidget QSpinBox#qt_calendar_yearspinbox {
                background-color: #71717A; 
                color: #FFEDD5;          
                border: none;
                font-size: 14px;
            }
            QCalendarWidget QSpinBox#qt_calendar_yearspinbox::up-button,
            QCalendarWidget QSpinBox#qt_calendar_yearspinbox::down-button {
                background-color: #52525B;
                width: 20px;
            }
            QCalendarWidget QSpinBox#qt_calendar_yearspinbox::up-button:hover,
            QCalendarWidget QSpinBox#qt_calendar_yearspinbox::down-button:hover {
                background-color: #F97316;
            }

            QCalendarWidget QMenu#qt_calendar_monthmenu {
                background-color: #3F3F46;
                color: #FFEDD5;         
                font-size: 14px;
            }

            QCalendarWidget QMenu#qt_calendar_monthmenu::item:selected {
                background-color: #F97316; 
                color: #A1A1AA;        
            }

            QCalendarWidget QAbstractItemView:enabled {
                background-color: #27272A; 
                color: #ffffff;      
                selection-background-color: #F97316;
                selection-color: #000000;       
            }
            QCalendarWidget QAbstractItemView:disabled {
                color: #a3a3a3;
            }
        """)

        header_format = QTextCharFormat()
        header_format.setForeground(QColor("#ffffff"))
        header_format.setBackground(QColor("#3F3F46"))
        header_format.setFontWeight(QFont.Bold)
        self.setHeaderTextFormat(header_format)

        weekend_format = QTextCharFormat()
        weekend_format.setForeground(QColor("#ffffff")) 
        weekend_format.setBackground(QColor("#52525B")) 
        self.setWeekdayTextFormat(Qt.Saturday, weekend_format)
        self.setWeekdayTextFormat(Qt.Sunday, weekend_format)

        today_format = QTextCharFormat()
        today_format.setBackground(QColor("#FFEDD5"))
        today_format.setForeground(QColor("#27272A"))
        today_format.setFontWeight(QFont.Bold)
        self.setDateTextFormat(QDate.currentDate(), today_format)