from utils.files import load_historic, load_reserves, load_cancel
from datetime import datetime

def full_cancels():
    cancel = load_cancel()
    total = 0
    print('canc', cancel)
    if cancel:
        for c in cancel:
            print(total)
            total += 1
            
        print('total', total)
        return f"{total}"
    
    else:
        return '0'

def total_value():
    historic = load_historic()
    
    total = 0
    total_gen = 0
    today = datetime.now().strftime("%d/%m/%Y")
    daily = {}
    if historic:
        for r in historic:
            date = r['date']
            daily[date] = daily.get(date, 0.0) + r['total_value']

            
            total_gen += r["total_value"]
            if r['date'] == today:
                total += r["total_value"]
        max_daily = max(daily.values()) if daily else 0
        print('Maximo:', max_daily)
        print('Daily:', daily)
        return f"R$ {total:.2f}".replace('.', ','), f"R$ {total_gen:.2f}".replace('.', ','), f"R$ {max_daily:.2f}".replace('.', ',')
    
    else:
        return True


def rooms_rented():
    reserves = load_reserves()
    
    total = 0
    name_room = ''
    if reserves:
        for r in reserves:
            if r['room'] != name_room:
                name_room = r['room']
                total += 1
        
        return f"{total}"
    
    return '0'

def total_rented():
    historic = load_historic()
    
    total = 0
    
    if historic:
        
        for h in historic:
            total += 1
        
        return f"{total}"
    

def cancel_rate():
    cancels = load_cancel()
    conclude = load_historic()
    
    total_cancel = 0
    total_conclude = 0
    
    for c in cancels:
        total_cancel += 1
    
    for c in conclude:
        total_conclude += 1
    
    rate = total_cancel * 100 / (total_conclude + total_cancel)
    
    return rate