from core.vector import *

class Entity:
    def __init__(self, name : str, gender : str, age : int, race : str, appearence : str, personality : str, background : str, note : str, position : Vector2D):
        self.name : str = name
        self.gender : str = gender
        self.age : int = age
        self.race : str = race
        self.appearence : str = appearence
        self.personality : str = personality
        self.background : str = background
        self.note : str = note
        self.position : Vector2D = position

    def to_dict(self):
        return {
            "name" : self.name,
            "gender" : self.gender,
            "age" : self.age,
            "race" : self.race,
            "appearence" : self.appearence,
            "personality" : self.personality,
            "background" : self.background,
            "note" : self.note,
            "positon" : self.position.to_dict()
        }