from utils.files import load_rooms, save_rooms, load_reserves

def add_room(name, value):
    rooms = load_rooms()
    if not any(r['name'] == name for r in rooms):
        rooms.append({'name': name, 'value': value})
        save_rooms(rooms)
        return True
    return False

def remove_room(name):
    rooms = load_rooms()
    reserves = load_reserves()
    
    for reserva in reserves:
        if reserva.get('room') == name:
            return False, f'Não é possível excluir essa sala pois {reserva.get("name", "alguém")} tem uma reserva dela!'
    
    updated_rooms = [room for room in rooms if room['name'] != name]
    if len(updated_rooms) < len(rooms):
        save_rooms(updated_rooms)
        return True, 'Sala removida com sucesso!'
    return False, 'Sala não encontrada!'