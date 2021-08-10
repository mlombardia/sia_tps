class Token():
    rowPos = 0
    colPos = 0
    symbol = ''
    def __init__(self):
        pass

class Player(Token):
    def __init__(self):
        super().__init__()
        self.symbol = '@'


class Box(Token):
    def __init__(self):
        super().__init__()
        self.symbol = '$'
