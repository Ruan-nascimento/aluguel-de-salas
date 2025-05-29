import json
import os


def load_rooms(path='src/services/salas.json'):
    
    try:
        with open(path, 'r') as room:
            return json.load(room)
    
    except FileNotFoundError:
        return True

def save_rooms(rooms, path='src/services/salas.json'):
    
    with open(path, 'w') as room:
        json.dump(room)


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