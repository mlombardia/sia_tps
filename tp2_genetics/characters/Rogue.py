from Character import Character

class Rogue(Character):

    def __init__(self, height, items):
        super().__init__()
        self.height = height
        self.performance = self.Performance()
        self.itemList = items
        self.DEFcte = 0.3
        self.ATTcte = 0.8

