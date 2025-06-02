import json
import os



def load_rooms(path='src/services/salas.json'):
    try:
        with open(path, 'r') as room:
            return json.load(room)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar salas: {e}")
        return []



def save_rooms(rooms, path='src/services/salas.json'):
    try:
        with open(path, 'w') as file:
            json.dump(rooms, file, indent=4)
        return True
    except Exception as e:
        print(f"Erro ao salvar salas: {e}")
        return False


def load_reserves(path='src/services/reservas.json'):
    
    try:
        with open(path, 'r') as reserve:
            return json.load(reserve)
    
    except FileNotFoundError:
        return True

def save_reserves(reserves, path='src/services/reservas.json'):
    
    with open(path, 'w') as r:
        json.dump(reserves, r, indent=4)
        

def load_historic(path='src/services/historico.json'):
    try:
        with open(path, 'r') as hist:
            return json.load(hist)
    except FileNotFoundError:
        return True

def save_historic(historic, path='src/services/historico.json'):
    with open(path, 'w') as hist:
        json.dump(historic, hist, indent=4)
        
def load_cancel(path='src/services/cancelamento.json'):
    try:
        with open(path, 'r') as hist:
            return json.load(hist)
    except FileNotFoundError:
        return True

def save_cancel(cancel, path='src/services/cancelamento.json'):
    with open(path, 'w') as hist:
        json.dump(cancel, hist, indent=4)