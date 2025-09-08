from core.config import *

class Stats:
    def __init__(self):
        self.stats = {}
        self.init_stats()

    def init_stats(self):
        self.stats = {}
        self.reset_stats()

    def reset_stats(self):
        self.stats = {key : 0 for key in statsKeysList}