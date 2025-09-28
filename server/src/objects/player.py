from src.core.inventory import *
from src.core.stats import *

from src.objects.entity import *

class Player(Entity):
    stats : Stats = Stats()
    inventory : Inventory = Inventory()