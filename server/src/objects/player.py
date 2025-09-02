from core.inventory import *
from core.stats import *

from objects.entity import *

class Player(Entity):
    def __init__(self, name, gender, age, race, appearence, personality, background, note, stats, inventory):
        super().__init__(name, gender, age, race, appearence, personality, background, note)
        self._stats : Stats = stats
        self.inventory : Inventory = inventory

    def to_dict(self):
        return {
            "player" : {
                **super().to_dict(),
                "stats" : self.stats
            }
        }
    
    @property
    def stats(self):
        return self._stats.stats