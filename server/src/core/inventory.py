from pydantic import BaseModel

class Inventory(BaseModel):
    slot : list[dict | None] = []
    max_slot : int = 30
    
    def add_item(self, item : dict):
        for i in range(self.max_slot):
            if (self.slot[i] == None):
                self.slot[i] = item

    def get_from_index(self, index : int):
        return self.slot[index]
    
    def get_from_name(self, name: str):
        for i in self.slot:
            if (self.slot[i]['name'] == name):
                return self.slot[i]