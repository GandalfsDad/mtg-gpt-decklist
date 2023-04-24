from dataclasses import dataclass
import inspect

class Card:

    def __init__(self, data, processed = False):
        self.__raw = data

        if processed:
            self.__processed = CardProperties(data)
        else:
            self.__processed = CardProperties.from_dict(data)

    def _process(self):
        return CardProperties(self.__raw)
    
    @property
    def id(self):
        return self.__raw['id']

    def __repr__(self):
        return self.__processed.embed_format()
    
@dataclass()
class CardProperties:
    name : str
    color_identity : str
    rarity : str
    set_name  : str
    power : str = None
    toughness : str = None
    loyalty : str = None
    oracle_text : str = None
    type_line : str = None
    mana_cost : str = None

    @classmethod
    def from_dict(cls, env):      
        return cls(**{
            k: v for k, v in env.items() 
            if k in inspect.signature(cls).parameters
        })
    
    def embed_format(self):
        return f"Name: {self.name} Type: {self.type_line} Mana Cost: {self.mana_cost} Color Identity: {self.color_identity} Text: {self.oracle_text} Rarity: {self.rarity} Power: {self.power} Toughness: {self.toughness} Loyalty: {self.loyalty}"