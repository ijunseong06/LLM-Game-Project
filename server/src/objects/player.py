from core.inventory import *
from core.stats import *

from objects.entity import *

class Player(Entity):
    stats : Stats = Stats()
    inventory : Inventory = Inventory()