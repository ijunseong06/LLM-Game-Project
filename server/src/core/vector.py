class Vector2D:
    def __init__(self):
        self.x : int = 0
        self.y : int = 0
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y
        }