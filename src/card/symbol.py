from ..util.data import get_data, load_data
import os

class SymbolMapper:
    def __init__(self):
        #check if fiel exists
        if os.path.exists('bin/symbology.json'):
            addition = load_data('bin/symbology.json')
        else:
            addition = get_data('https://api.scryfall.com/symbology', save=True, save_path='bin/symbology.json')
        self.__map = {i['symbol']:i['english'] for i in addition['data']}

    def map(self, input_string):
        for k,V in self.__map.items():
            input_string = input_string.replace(k, f"{V} ")
        return input_string