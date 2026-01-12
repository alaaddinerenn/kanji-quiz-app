import json
import os

def load_kanji_data(file_path=None):
    if file_path is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "data", "kanji_data.json")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # If data is a dict with 'kanji' key, extract the list
    if isinstance(data, dict) and 'kanji' in data:
        return data['kanji']
    
    return data

def get_kanji_meanings(kanji_data):
    if not isinstance(kanji_data, list):
        raise ValueError(f"Expected list, got {type(kanji_data)}")
    
    return {kanji['character']: kanji['meanings'] for kanji in kanji_data}

def get_kanji_readings(kanji_data):
    if not isinstance(kanji_data, list):
        raise ValueError(f"Expected list, got {type(kanji_data)}")
    
    return {kanji['character']: (kanji['onyomi'], kanji['kunyomi']) for kanji in kanji_data}