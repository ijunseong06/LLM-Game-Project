from core.stats import *

class Item:
    def __init__(self, name, description, stats):
        self.name : str = name
        self.description : str = description
        self.stats : Stats = stats