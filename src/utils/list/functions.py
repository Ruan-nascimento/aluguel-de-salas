from utils.files import load_reserves, load_historic, save_reserves, save_historic
from PyQt5.QtWidgets import QTableWidgetItem
from components.nav_buttons import Button

def load_all_reserves(table, concluir, cancelar):
    reserves = load_reserves()
    
    table.setRowCount(len(reserves))
    
    for i, r in enumerate(reserves):
        table.setItem(i, 0, QTableWidgetItem(r["name"]))
        table.setItem(i, 1, QTableWidgetItem(r["room"]))
        table.setItem(i, 2, QTableWidgetItem(r["date"]))
        table.setItem(i, 3, QTableWidgetItem(r["in_hour"]))
        table.setItem(i, 4, QTableWidgetItem(r["out_hour"]))
        table.setItem(i, 5, QTableWidgetItem(f"R${r['total_value']:.2f}"))
        
        ready_button = Button('Concluir').button
        cancel_button = Button('Cancelar').button
        cancel_button.setStyleSheet("""
                                       QPushButton {
                                        background-color: #8b8b8b;
                                        color: white;
                                        outline: none;
                                        border-radius: 8px;
                                        padding: 10px
                                    }
                           
                                        QPushButton:hover{
                                            background-color: #575757;
                                        }
                                       """)
        
        ready_button.clicked.connect(lambda _, index=i: concluir(index))
        table.setCellWidget(i, 6, ready_button)
        
        cancel_button.clicked.connect(lambda _, index=i: cancelar(index))
        table.setCellWidget(i, 7, cancel_button)
        

def conclude_reserves(i):
    reserves = load_reserves()
    
    if 0 <= i < len(reserves):
        historic = load_historic()
        conclude = reserves.pop(i)
        historic.append(conclude) 
        save_reserves(reserves)
        save_historic(historic)
        return True
    
    return False

def cancel_reserves(i):
    
    reserves = load_reserves()
    if 0 <= i < len(reserves):
        reserves.pop(i)
        save_reserves(reserves)
        return True

    return False