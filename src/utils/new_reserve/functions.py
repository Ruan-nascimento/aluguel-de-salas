from utils.files import load_rooms, load_reserves, save_reserves

def update_rooms():
    rooms = load_rooms()
    if not rooms == True:
        if rooms:
            return [r['name'] for r in rooms]
            
                
        else:
            return ["Nenhuma sala encontrada!"]
    
    else:
        return True


def create_reserve(name, room, date, in_hour, out_hour):
    reserves = load_reserves()
    rooms = load_rooms()
    
    if not reserves == True and not rooms == True:
        min_in = int(in_hour.split(':')[0]) * 60 + int(in_hour.split(':')[1])
        min_out = int(out_hour.split(':')[0]) * 60 + int(out_hour.split(':')[1])
        
        if min_out <= min_in:
            return False, "Horário de Saída deve ser maior que o de entrada!"
        
        for r in reserves:
            if r["room"] == room and r["date"] == date:
                r_in = int(r["in_hour"].split(":")[0]) * 60 + int(r["in_hour"].split(":")[1])
                r_out = int(r["out_hour"].split(":")[0]) * 60 + int(r["out_hour"].split(":")[1])
                
                if not (r_out <= r_in or r_in >= r_out):
                    return False, "Dia e Horário Indisponivel Para Essa Sala!"
        
        
        room_info = next((r for r in rooms if r["name"] == room), None)
        value_hour = room_info["value"]
        total_hour = (min_out - min_in) / 60
        total_value = value_hour * total_hour
        
        new_reserve = {
            "name": name,
            "room": room,
            "date": date,
            "in_hour": in_hour,
            "out_hour": out_hour,
            "total_value": total_value
        }
        
        reserves.append(new_reserve)
        save_reserves(reserves)
        
        return True, f"Reservado Com Sucesso! \n Custo Total de R$ {total_value:.2f}"